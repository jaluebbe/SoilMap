import sys
# https://github.com/jaluebbe/HeightMap
sys.path.append('../HeightMap')
# GEBCO 2019 provides world wide coverage of elevation and seafloor bathymetry
# in a 15 arc second grid (12 GB disk space required).
import height_map.gebco_2019 as gebco_2019
# https://github.com/jaluebbe/SurfaceMap
sys.path.append('../SurfaceMap')
from surface_map.globcover2009 import GlobCover2009
from surface_map.udel_airt_precip import UDelAirTPrecip
from soil_map.soil_ph_in_h2o import SoilPHinH2O
from soil_map.modis_lst import ModisLST

gc = GlobCover2009()
precip = UDelAirTPrecip(air_temp=False)
sph = SoilPHinH2O()
m_lst = ModisLST()

def get_environmental_data(lat, lon):
    result = {}
    result['altitude_m'] = gebco_2019.get_height(lat, lon)['altitude_m']
    result['annual_precip_cm'] = precip.get_data_at_position(lat, lon)[
        'annual_precip_cm']
    result['soil_ph_in_h2o'] = sph.get_data_at_position(lat, lon)[
        'soil_ph_in_h2o']
    temperatures = m_lst.get_data_at_position(lat, lon)
    result['min_surface_temp'] = temperatures['min_surface_temp']
    result['max_surface_temp'] = temperatures['max_surface_temp']
    result['daily_surface_temp_range'] = temperatures['daily_surface_temp_range']
    result['surface_information'] = gc.get_data_at_position(lat, lon)
    return result
