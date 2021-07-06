from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class TaxInfo(Base):
    __tablename__ = 'tax_info'

    id = Column(Integer, primary_key=True)
    comercial_info = Column(String)
    company = relationship('company')
    company_id = Column(Integer,ForeignKey('company.id'),unique=True)

    def __repr__(self):
        return f'(ID:{self.id}),(Comercial Info:{self.comercial_info})'
