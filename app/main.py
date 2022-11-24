import os

import h3
from fastapi import FastAPI, Depends
from sqlalchemy import func

from app.db.database import Session, get_db
from app.db.repository import calculate_aggregation
from app.db.schemas import AggregationWithinRadiusIn, AggregationInPolygonIn

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

resolution = 11

aggregate_function = {
    "sum": func.sum,
    "avg": func.avg,
    "min": func.min,
    "max": func.max,
}

app = FastAPI()


@app.post("/aggregation_within_radius")
async def calculate_aggregation_within_radius_of_k_hexes(
        parameters: AggregationWithinRadiusIn,
        db: Session = Depends(get_db)
):
    cell = h3.geo_to_h3(parameters.geometry.coordinates[1], parameters.geometry.coordinates[0], resolution)
    ring = h3.k_ring(cell, parameters.r)
    ring_geometry = h3.h3_set_to_multi_polygon(ring, geo_json=True)

    return calculate_aggregation(db, aggr=parameters.aggr, field=parameters.field, geometry=ring_geometry)


@app.post("/aggregation_in_polygon")
async def calculate_aggregation_in_polygo(
        parameters: AggregationInPolygonIn,
        db: Session = Depends(get_db)
):
    parameters.geometry.coordinates = [[pair[::-1] for pair in row] for row in parameters.geometry.coordinates]
    cells = h3.polyfill(parameters.geometry.dict(), resolution)
    cells_geometry = h3.h3_set_to_multi_polygon(cells, geo_json=True)

    return calculate_aggregation(db, aggr=parameters.aggr, field=parameters.field, geometry=cells_geometry)
