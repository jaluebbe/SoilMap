import os
import json
from soil_map.geotiff_handler import GeoTiffHandler

class ModisLST:

    path = 'soil_map/maps/modis_lst'
    attribution_url = ('https://doi.org/10.5281/zenodo.1435938')
    attribution_name = 'MODIS LST'
    attribution = ('&copy <a href="{}">{}</a>').format(attribution_url,
        attribution_name)

    def __init__(self):
        self.gth_t_low = GeoTiffHandler(os.path.join(self.path,
            'clm_lst_mod11a2.jan.night_l.025_1km_s0..0cm_2000..2017_v1.0.tif'))
        self.gth_t_high = GeoTiffHandler(os.path.join(self.path,
            'clm_lst_mod11a2.jul.day_u.975_1km_s0..0cm_2000..2017_v1.0.tif'))
        self.gth_t_range = GeoTiffHandler(os.path.join(self.path,
            'clm_lst_mod11a2.apr.daynight_m_1km_s0..0cm_2000..2017_v1.0.tif'))

    def get_min_surface_temp(self, lat, lon):
        data = self.gth_t_low.get_value_at_position(lat, lon)
        if data is not None:
            return data * 0.02 - 273.15
        return float('NaN')

    def get_max_surface_temp(self, lat, lon):
        data = self.gth_t_high.get_value_at_position(lat, lon)
        if data is not None:
            return data * 0.02 - 273.15
        return float('NaN')

    def get_surface_temp_range(self, lat, lon):
        data = self.gth_t_range.get_value_at_position(lat, lon)
        if data is not None:
            return data * 0.02
        return float('NaN')

    def get_data_at_position(self, lat, lon):
        return {
            'min_surface_temp': round(self.get_min_surface_temp(lat, lon), 2),
            'max_surface_temp': round(self.get_max_surface_temp(lat, lon), 2),
            'daily_surface_temp_range': round(self.get_surface_temp_range(
                lat, lon), 2),
            'source': self.attribution_name, 'attribution': self.attribution}
