import os
from django.contrib.gis.utils import LayerMapping
from .models import BlueEarth

blueearth_mapping = {
    'areasymbol' : 'AREASYMBOL',
    'spatialver' : 'SPATIALVER',
    'musym' : 'MUSYM',
    'mukey' : 'MUKEY',
    'geom' : 'MULTIPOLYGON',
}

be_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/soilmu_a_mn013.shp'))
def run(verbose=True):
	lm = LayerMapping(BlueEarth, be_shp, blueearth_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)
