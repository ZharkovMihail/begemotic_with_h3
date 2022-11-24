from typing import Literal

from geoalchemy2 import WKTElement
from sqlalchemy import func
from sqlalchemy.orm import Session

from .models import Apartments


aggregate_function = {
    "sum": func.sum,
    "avg": func.avg,
    "min": func.min,
    "max": func.max,
}


def calculate_aggregation(
        db: Session,
        *,
        field: Literal["apartments", "price", "year"],
        aggr: Literal["sum", "avg", "min", "max"],
        geometry: list
):
    polygon = ""
    for point in geometry[0][0]:
        polygon += f"{point[0]} {point[1]}, "
    polygon = WKTElement(f'POLYGON(({polygon[:-2]}))', srid=4326)

    return db.query(aggregate_function[aggr](Apartments.__table__.c[field]).
                    label(aggr)).filter(func.ST_DWithin(Apartments.geopos, polygon, 0)).first()
