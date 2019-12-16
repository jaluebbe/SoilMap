import os
import json
from soil_map.geotiff_handler import GeoTiffHandler

class SoilWaterContent:

    path = 'soil_map/maps/soil_water_content'
    attribution_url = ('https://doi.org/10.5281/zenodo.2784001')
    attribution_name = 'soil water content (LandGIS)'
    attribution = ('&copy <a href="{}">{}</a>').format(attribution_url,
        attribution_name)

    def __init__(self):
        self.gth_soil_water_content = GeoTiffHandler(os.path.join(self.path,
            'sol_watercontent.33kPa_usda.4b1c_m_250m_b100..100cm_1950..2017_v0'
            '.1.tif'))

    def get_soil_water_content(self, lat, lon):
        return self.gth_soil_water_content.get_value_at_position(lat, lon)

    def get_data_at_position(self, lat, lon):
        return {
            'soil_water_content_percent': self.get_soil_water_content(lat, lon),
            'source': self.attribution_name, 'attribution': self.attribution}
