"""Add apartments
Revision ID: 7df1cc3e34f6
Revises: 60f797d4f828
Create Date: 2022-11-17 22:04:47.372921
"""
import csv
import json

from alembic import op
from geoalchemy2.shape import from_shape
from shapely.geometry import shape

# revision identifiers, used by Alembic.
from app.db.models import Apartments
from app.main import ROOT_DIR

revision = '7df1cc3e34f6'
down_revision = '449ceda5a897'
branch_labels = None
depends_on = None


def upgrade():

    apartments = []
    with open(f'{ROOT_DIR}/apartments.csv', mode='r') as csvfile:
        for row in csv.DictReader(csvfile, skipinitialspace=True):
            apartment = {}
            for k, v in row.items():
                if k == "geopos":
                    v = from_shape(shape(json.loads(v.replace("\'", "\""))))
                elif k == "price":
                    v = float(v)
                elif k in ("id", "apartments", "year"):
                    v = int(v)
                else:
                    raise
                apartment[k] = v
            apartments.append(apartment)

    op.bulk_insert(Apartments.__table__, apartments)


def downgrade():
    pass