import os
import json
from soil_map.geotiff_handler import GeoTiffHandler

class SoilPHinH2O:

    path = 'soil_map/maps/soil_ph_in_h2o'
    attribution_url = ('https://doi.org/10.5281/zenodo.2525664')
    attribution_name = 'soil pH in H2O (LandGIS)'
    attribution = ('&copy <a href="{}">{}</a>').format(attribution_url,
        attribution_name)

    def __init__(self):
        self.gth_soil_ph_in_h2o = GeoTiffHandler(os.path.join(self.path,
            'sol_ph.h2o_usda.4c1a2a_m_250m_b100..100cm_1950..2017_v0.2.tif'))

    def get_soil_ph_in_h2o(self, lat, lon):
        data = self.gth_soil_ph_in_h2o.get_value_at_position(lat, lon)
        if data is not None:
            return data / 10
        return float('NaN')

    def get_data_at_position(self, lat, lon):
        return {
            'soil_ph_in_h2o': self.get_soil_ph_in_h2o(lat, lon),
            'source': self.attribution_name, 'attribution': self.attribution}
