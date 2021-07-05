import os

from models.database import DATABASE_NAME
import create_database as db_creator
from models.room import Room
from models.building import Building
from models.equipmnet import Equipment
from models.company import Company
from models.electrical import Electrical
from models.mechanical import Mechanical
from models.tax_info import TaxInfo

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_db()
