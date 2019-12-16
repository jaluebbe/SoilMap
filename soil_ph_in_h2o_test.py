from soil_map.soil_ph_in_h2o import SoilPHinH2O

sph = SoilPHinH2O()
print('London', sph.get_data_at_position(51.5, -0.12))
print('Black Forest', sph.get_data_at_position(47.94, 8.3))
print('high moor in Emsland region', sph.get_data_at_position(52.8, 7.4))
print('Salt Lake City', sph.get_data_at_position(40.8, -112))
print('Death Valley', sph.get_data_at_position(36.247, -116.817))
