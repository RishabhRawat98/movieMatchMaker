from datetime import datetime
from flaskmov import db, login_manager
from flask_login import UserMixin
from io import TextIOWrapper
import csv


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Moviedata(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   number = db.Column(db.Integer)
   overview = db.Column(db.Text)
   poster_path = db.Column(db.Text)
   release_date = db.Column(db.Text)
   title = db.Column(db.Text)
   genre1 = db.Column(db.Integer)
   genre2 = db.Column(db.Integer)


   def __repr__(self):
           return f"('{self.title}', '{self.overview}','{self.poster_path}', '{self.release_date}','{self.genre1}', '{self.genre2}')"



class UserWatchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UserWatchlist {}>'.format(self.title, self.user_id)


class DontWatchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<DontWatchlist {}>'.format(self.title, self.user_id)

class RecomendedList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    # movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<RecomendedList {}>'.format(self.title)

###################################################################################### Dodgey code



# file_name = "D:\\AuthWorking\\06-Login-Auth\\flaskblog\\Use.csv"

# def runner():
#     with open(file_name, 'r', encoding='utf-8') as f:
#         new_reader = csv.reader(f)
#         rows=list(new_reader)
#         for row in rows:
#             movie = Moviedata(number=row[0],overview=row[1]
#             ,poster_path=row[2],release_date=row[3],title=row[4],
#             genre1=row[5], genre2=row[6])
#             db.session.add(movie)
#             db.session.commit()

# runner()