import urllib.parse as urllib_parse
import concurrent.futures
from mappers.Mapper import Mapper
from models import db
from models.Lunettes import Lunettes
from models.Categorie import Categorie
from models.Form import Form
from models.Gender import Gender
from models.Marque import Marque
from models.Material_Fond import Material_Fond
from models.Material_Front import Material_Front
from models.Structure import Structure
from models.Taille_Lunettes import Taille_Lunettes
from models.Taille_Temple import Taille_Temple

from sqlalchemy.orm import scoped_session
class LunetteMap(Mapper):
    _class_name = 'woocommerce-product-attributes-item__value'
    # _class_name = 'woocommerce-product-attributes shop_attributes'
    def mapModels(self, url:str):
        self.loadPage(url)
        self.logger.info("Started fetching model links")
        pages = self.getGlassesLinks()
        self.logger.info("Finished fetching model links")
        self.logger.info("Started Scrapping all lunettes models")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            pageContents = executor.map(self.getBaseElement, pages)
            self.models = [
                self.buildModel(baseElement)
                for baseElement in pageContents
            ]
            self.logger.info("Scrapped all lunettes models")

    def getPageLinks(self):
        pageLink = urllib_parse.urlparse(
            self.scrapper.getElementsByClass("page-numbers")[3]["href"]
            )
        lastPage = pageLink.path.split(sep = '/')[3]
        pages = range(1, int(lastPage) + 1)
        return [f"https://contrastlens.com/boutique/page/{page}/"
                    for page in pages]
    
    def getGlassesLinks(self):
        links = []
        pages = self.getPageLinks()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                results = executor.map(self.getGlassesLinksInPage, pages)
                for result in results: 
                    links.extend(result)
            except concurrent.futures.CancelledError as error:
                self.logger.error(f"getGlassesLinks => {error.filename} => {error.strerror}")
        return links

    def getGlassesLinksInPage(self, page:str):
        self.loadPage(page)
        links = [el.get('href')
            for el in self.scrapper.getElementsByClass("show_details_button")]
        return links

    def getBaseElement(self, url:str):
        self.loadPage(url)
        base_class_name = 'woocommerce-product-attributes-item--attribute_pa_'
        self.logger.info('Started Scrapping for Lunettes')
        contents = (
            self.scrapper.getElementsByClass(base_class_name + "marque"),
            self.scrapper.getElementsByClass(base_class_name + "categorie"),
            self.scrapper.getElementsByClass(base_class_name + "gender"),
            self.scrapper.getElementsByClass(base_class_name + "shape"),
            self.scrapper.getElementsByClass(base_class_name + "structure"),
            self.scrapper.getElementsByClass(base_class_name + "front-material"),
            self.scrapper.getElementsByClass(base_class_name + "temple-material"),
            self.scrapper.getElementsByClass(base_class_name + "taille"),
            self.scrapper.getElementsByClass(base_class_name + "temple-size"),
            self.scrapper.getElementsByClass(base_class_name + "annee")
        )
        self.logger.info('Finished scrapping for Lunettes')
        return (el[0].a.string if len(el) != 0 else None for el in contents)

    def buildModel(self, elements):

        # Values from html
        marque_content, categorie_content, gender_content,\
            form_content, structure_content, materialFront_content,\
            materialFond_content,  taille_content, tailleTemple_content,\
            year\
            =elements
        
        
        # Correspondant Ids
        session = db()
        def queryBuilder(columnName, name):
            if name is None:
                self.logger.warning(f'Found a None value for {columnName}')
            return session.query(columnName).filter_by(name = name)\
                .one().id \
                if name is not None \
                else None
        try:
            m = Lunettes(
                id=None, 
                categorie_id = queryBuilder(Categorie.id, categorie_content),
                form_id = queryBuilder(Form.id, form_content),
                gender_id = queryBuilder(Gender.id, gender_content),
                marque_id = queryBuilder(Marque.id, marque_content),
                material_fond_id = queryBuilder(Material_Fond.id, materialFond_content),
                material_front_id = queryBuilder(Material_Front.id, materialFront_content),
                structure_id = queryBuilder(Structure.id, structure_content),
                taille_lunettes_id = queryBuilder(Taille_Lunettes.id, taille_content),
                taille_temple_id = queryBuilder(Taille_Temple.id, tailleTemple_content),
                year = year
            )
            session = scoped_session(db)
            session.add(m)
            session.commit()
            session.remove()
            return m
        except Exception as err:
            self.logger.error(f"buildModel => {err.args}")
            return None