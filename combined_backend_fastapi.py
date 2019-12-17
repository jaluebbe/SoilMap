from fastapi import FastAPI, Query
import math
import combined_backend as cb

app = FastAPI()

@app.get("/api/get_environmental_data")
def get_environmental_data(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180)
    ):
    environmental_data = cb.get_environmental_data(lat, lon)
    for key in ['annual_precip_cm', 'soil_ph_in_h2o', 'min_surface_temp',
            'max_surface_temp', 'daily_surface_temp_range']:
        if math.isnan(environmental_data[key]):
            environmental_data[key] = 'NaN'
    return environmental_data
