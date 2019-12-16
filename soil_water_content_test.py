from soil_map.soil_water_content import SoilWaterContent

swc = SoilWaterContent()
print('London', swc.get_data_at_position(51.5, -0.12))
print('Black Forest', swc.get_data_at_position(47.94, 8.3))
print('high moor in Emsland region', swc.get_data_at_position(52.8, 7.4))
print('Salt Lake City', swc.get_data_at_position(40.8, -112))
print('Death Valley', swc.get_data_at_position(36.247, -116.817))
