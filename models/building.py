from sqlalchemy import Table, Column, Integer, String, ForeignKey
from models.database import Base

association_table = Table('building_companies', Base.metadata,
                          Column('building_name', Integer, ForeignKey('company.name')),
                          Column('building.addres', String, ForeignKey('company.addres')))


class Building(Base):
    __tablename__ = 'building'

    id = Column(Integer, primary_key=True)
    addres = Column(String, ForeignKey('room.id'))
    name = Column(String)

    def __init__(self, addres: str, name: str):
        self.addres = addres
        self.name = name

    def __repr__(self):
        return f'(Building ID:{self.id}),(Building Adress:{self.addres}),(Building name:{self.name})'
