from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:kulundu1999@localhost:5432/library1")
Base = declarative_base()

class Books(Base):
    __tablename__ = 'Books'

    id = Column(Integer, Sequence('books_id_seq'), primary_key=True)
    author = Column(String(255), nullable=False)
    descrip = Column(String(500), nullable=False)
    year = Column(String(255), nullable=False)



Base.metadata.create_all(engine)
