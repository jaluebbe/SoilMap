import json
import combined_backend as cb
# https://github.com/jaluebbe/GPSTracker
file_name = '../GPSTracker/artificial_tracking_data.json'
with open(file_name, 'r') as f:
    track_data = json.load(f)
new_track_data = []
for segment in track_data[0]['features']:
    for location in segment['geometry']['coordinates']:
        lat = location[1]
        lon = location[0]
        new_track_data.append(cb.get_environmental_data(lat, lon))

print(new_track_data)
