# models.py
# from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

def Load_movies(file_name):
    data = csv.reader(file_name, delimiter = ',')
    return data.tolist()

Base = declarative_base()

class Movdb(Base):
    __tablename__ = 'movdb'
    __table_args_ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    overview = Column(VARCHAR)
    poster_path = Column(VARCHAR)
    release_date = Column(VARCHAR)
    title = Column(VARCHAR)
    genre1 = Column(Integer)
    genre2 = Column(Integer)
    children = relationship('Watchls')



engine = create_engine('sqlite:///plswork.db')
Base.metadata.create_all(engine)
file_name = 'Use.csv'
# df = pd.read_csv(file_name)
df.to_sql(con=engine, index_label='id', name=Movdb.__tablename__, if_exists='replace')
Session = sessionmaker(bind=engine)
session = Session()

movie = session.query(Movdb)

for m in movie:
    print(m.title, m.id, m.poster_path)

