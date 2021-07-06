from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.equipmnet import Equipment


class Electrical(Equipment):
    power_configuration = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'electrical'
    }
