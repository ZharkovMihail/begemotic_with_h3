from typing import Literal

from pydantic import BaseModel, PositiveInt
from geojson_pydantic.geometries import Point, Polygon


class AggregationWithinRadiusIn(BaseModel):
    geometry: Point
    field: Literal["apartments", "price", "year"]
    aggr: Literal["sum", "avg", "min", "max"]
    r: PositiveInt


class AggregationInPolygonIn(BaseModel):
    geometry: Polygon
    field: Literal["apartments", "price", "year"]
    aggr: Literal["sum", "avg", "min", "max"]
