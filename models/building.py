from sqlalchemy import Table, Column, Integer, String, ForeignKey
from models.database import Base

association_table = Table('building_companies', Base.metadata,
                          Column('building_id', Integer, ForeignKey('building.id')),
                          Column('company_id', Integer, ForeignKey('company.id')))


class Building(Base):
    __tablename__ = 'building'

    id = Column(Integer, primary_key=True)
    name = Column(String)
