# models.py
# from numpy import genfromtxt
# from time import time
# from datetime import datetime
# from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# def Load_movies(file_name):
#     data = csv.reader(file_name, delimiter = ',')
#     return data.tolist()

# Base = declarative_base()

# class Movdb(Base):
#     __tablename__ = 'movdb'
#     __table_args_ = {'sqlite_autoincrement': True}
#     id = Column(Integer, primary_key=True, nullable=False)
#     overview = Column(VARCHAR)
#     poster_path = Column(VARCHAR)
#     release_date = Column(VARCHAR)
#     title = Column(VARCHAR)
#     genre1 = Column(Integer)
#     genre2 = Column(Integer)
#     children = relationship('Watchls')



# engine = create_engine('sqlite:///plswork.db')
# Base.metadata.create_all(engine)
# file_name = 'Use.csv'
# # df = pd.read_csv(file_name)
# df.to_sql(con=engine, index_label='id', name=Movdb.__tablename__, if_exists='replace')
# Session = sessionmaker(bind=engine)
# session = Session()

# movie = session.query(Movdb)

# for m in movie:
#     print(m.title, m.id, m.poster_path)
###########################THe good code 
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy 
# import csv
# from io import TextIOWrapper

# app = Flask(__name__)
# app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///znewmovie.db'
# db = SQLAlchemy(app)

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String)

# #     def __repr__(self):
# #         return f"User('{self.username}')"


# #,overview,poster_path,release_date,title,genre1,genre2

# class Moviedata(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    number = db.Column(db.Integer)
#    overview = db.Column(db.Text)
#    poster_path = db.Column(db.Text)
#    release_date = db.Column(db.Text)
#    title = db.Column(db.Text)
#    genre1 = db.Column(db.Integer)
#    genre2 = db.Column(db.Integer)

#    def __repr__(self):
#        return f"Moviedata('{self.title}', '{self.overview}', '{self.poster_path}', '{self.release_date}', '{self.genre1}', '{self.genre2}')"


# db.create_all()


# file_name = "Use.csv"

# def runner():
#     with open(file_name, 'r', encoding='utf-8') as f:
#         new_reader = csv.reader(f)
#         # new_reader = TextIOWrapper(new_reader, encoding='utf-8')
#         # rows = csv.reader(new_reader, delimiter=',')
#         rows=list(new_reader)
#         print(rows[0])
#         for row in rows:
#             movie = Moviedata(number=row[0],overview=row[1], poster_path=row[2], release_date=row[3], title=row[4], genre1=row[5], genre2=row[6])
#             db.session.add(movie)
#             db.session.commit()
#             # print(row[0])


# runner()


# #This is what the columns for the sql are 
# # number,overview,poster_path,release_date,title,genre1,genre2 
