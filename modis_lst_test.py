from soil_map.modis_lst import ModisLST

m_lst = ModisLST()
print('London', m_lst.get_data_at_position(51.5, -0.12))
print('Black Forest', m_lst.get_data_at_position(47.94, 8.3))
print('high moor in Emsland region', m_lst.get_data_at_position(52.8, 7.4))
print('Salt Lake City', m_lst.get_data_at_position(40.8, -112))
print('Death Valley', m_lst.get_data_at_position(36.247, -116.817))
