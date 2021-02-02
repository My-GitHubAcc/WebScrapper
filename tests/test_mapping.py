from models.Lunettes import Lunettes
import re

from mappers.CategorieMap import CategorieMap, Categorie
from mappers.FormMap import FormMap, Form
from mappers.GenderMap import GenderMap, Gender
from mappers.MarqueMap import MarqueMap, Marque
from mappers.MaterialFondMap import MaterialFondMap, Material_Fond
from mappers.MaterialFrontMap import MaterialFrontMap, Material_Front
from mappers.MaterialLensMap import MaterialLensMap, Material_Lens
from mappers.StructureMap import StructureMap, Structure
from mappers.TailleTempleMap import TailleTempleMap, Taille_Temple
from mappers.TailleLunettesMap import TailleLunettesMap, Taille_Lunettes
from models import db
from mappers.LunetteMap import LunetteMap

import concurrent.futures
class TestMapping:
    url = "http://contrastlens.com/"

    def test_can_fetch_models_properly(self):
        maps = [
            CategorieMap(),
            FormMap(),
            GenderMap(),
            MaterialFondMap(),
            MaterialFrontMap(),
            MaterialLensMap(),
            MarqueMap(),
            StructureMap(),
            TailleTempleMap(),
            TailleLunettesMap()
            ]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            fs = [executor.submit(m.mapModels, self.url + 'boutique') for m in maps]
            for _ in concurrent.futures.as_completed(fs): 
                continue

        models = []
        for m in maps:
            assert len(m.models) > 0
            models.extend(m.models)


        session = db()
        session.add_all(models)
        session.commit()

    # def test_models_can_be_saved(self):
    #     tailleLunettesMap = TailleLunettesMap()
    #     tailleLunettesMap.mapModels(self.url + 'boutique')
    #     assert tailleLunettesMap.models
    #     session = db()
    #     session.add_all(tailleLunettesMap.models)
    #     session.commit()
    #     categorieMap.saveToDb(create_engine('sqlite:///db.sqlite'))

    def test_can_fetch_all_catalog_pages(self):
        map = LunetteMap()
        map.loadPage(self.url + 'boutique')
        pages = map.getPageLinks()

        assert len(pages) > 0

    def test_can_fetch_all_page_links_for_models_from_single_page(self):
        map = LunetteMap()
        map.loadPage(self.url + 'boutique')
        pages = map.getPageLinks()
        modelLinks = map.getGlassesLinksInPage(pages[0])

        assert len(map.scrappers) == 0
        assert len(modelLinks) > 0
    
    def test_can_fetch_all_page_links_for_models_from_available_page(self):
        map = LunetteMap()
        map.loadPage(self.url + 'boutique')
        modelLinks = map.getGlassesLinks()

        assert len(modelLinks) > 0
    
    def test_can_make_an_object(self):
        model = Lunettes(
                id=None, name=None,
                categorie_id = None,
                form_id = None,
                gender_id = None,
                marque_id = None,
                material_fond_id = None,
                material_front_id = None,
                structure_id = None,
                taille_lunettes_id = None,
                taille_temple_id = None,
                year = None
            )
        assert model

    def test_is_able_to_build_a_lunette(self):
        map = LunetteMap()
        glassesNames = ["dior-diorama1", "db-1016", "tommy-hilfiger-th-1733", "mos008-s"]
        m = []
        for name in glassesNames:
            elements = map.getBaseElement(self.url + f'produit/{name}')
            m.append(map.buildModel(elements))
        assert len(m) == 4

    def test_all_glasses_can_be_succefully_mapped(self):
        map = LunetteMap()
        map.loadPage(self.url + 'boutique')
        pages = map.getGlassesLinks()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            pageContents = executor.map(map.getBaseElement, pages)
            # Nones = len(el for el in pageContents if el[3] is None)
            
            map.models = [
                map.buildModel(baseElement)
                for baseElement in pageContents
            ]
        assert len(map.models) > 0

    def test_can_save_lunettes_to_db(self):
        map = LunetteMap()
        map.mapModels(self.url + 'boutique')

        assert len(map.models) > 0