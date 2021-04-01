from mappers.CategorieMap import CategorieMap
from mappers.FormMap import FormMap
from mappers.GenderMap import GenderMap
from mappers.MarqueMap import MarqueMap
from mappers.MaterialFondMap import MaterialFondMap
from mappers.MaterialFrontMap import MaterialFrontMap
from mappers.MaterialLensMap import MaterialLensMap
from mappers.StructureMap import StructureMap
from mappers.TailleTempleMap import TailleTempleMap
from mappers.TailleLunettesMap import TailleLunettesMap
from models import db
from mappers.LunetteMap import LunetteMap

import concurrent.futures
url = "http://contrastlens.com/"

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
    fs = [executor.submit(m.mapModels, url + 'boutique') for m in maps]
    for _ in concurrent.futures.as_completed(fs): 
        continue

models = []
for m in maps:
    assert len(m.models) > 0
    models.extend(m.models)

session = db()
session.add_all(models)
session.commit()

map = LunetteMap()
map.mapModels(url + 'boutique')