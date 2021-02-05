from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import csv
from io import TextIOWrapper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



#,overview,poster_path,release_date,title,genre1,genre2

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
    #    return f"Moviedata('{self.title}', '{self.overview}', '{self.poster_path}', '{self.release_date}', '{self.genre1}', '{self.genre2}')"
           return f"('{self.title}', '{self.overview}', '{self.poster_path}', '{self.release_date}', '{self.genre1}', '{self.genre2}')"




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    watched = db.relationship('UserWatchlist', backref='author',lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)



# class Watchls(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    


#     def __repr__(self):
#         return '<Post {}>'.format(self.id)



# class Dontwatchls(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


class UserWatchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UserWatchlist {}>'.format(self.title, self.user_id)

class nols(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<nols {}>'.format(self.title, self.user_id)





# file_name = "Use.csv"

# def runner():
#     with open(file_name, 'r', encoding='utf-8') as f:
#         new_reader = csv.reader(f)
#         rows=list(new_reader)
#         # print(rows[0])
#         for row in rows:
#             movie = Moviedata(number=row[0],overview=row[1], poster_path=row[2], release_date=row[3], title=row[4], genre1=row[5], genre2=row[6])
#             db.session.add(movie)
#             db.session.commit()
#             # print(row[0])


# runner()
db.create_all()
user_1 = User(username='Thebroshab', email='dragod@gmail.com')
user_2 = User(username='Ezclap', email='Ezclap@gmail.com')
# watch_1 = UserWatchlist(title='Moonlight', user_id=1)
# db.session.add(user_1)
# db.session.add(user_2)
# db.session.add(watch_1)
# db.session.delete(UserWatchlist.query.get(1))
db.session.commit()

# tst_user = User.query.all()
# print(tst_user)
# def usegetter():
#     for u in tst_user:
#         # print(u.id, u.username, u.email)
#         print('only user name' + u.username)

# tst_user = User.query.all()
# for user in tst_user:
#     print(user.username)
# usegetter()
# def movlist():
#     for mov in mov_list_obj:
#         name_mov = mov.title
#     return name_mov
# f_us = User.query.get(61)
# print(f_us.username, f_us.email)


# try:
#     s = UserWatchList.query.get(2)

#     print(s)
# except NameError:
#     print('Workin bby')


#If no UserWatchList is empty then it comes us as name UserWatchList is not defined

# tst_mov = Moviedata.query.all()

# def mov_get():
#     for mov in tst_mov:
#         m_name = [mov.title]
#         m_rel = [mov.release_date]
#     return m_name, m_rel

# print(mov_get())

# check = Moviedata.query.get(1)
# lstc = list(check)
# print(lstc)

# check = Moviedata.query.all()
# nls = []
# for m in check:
#     nls.append(m.title)
    
# print(nls)    

# check2 = nols.query.all()
# nls = []
# for m in check2:
#     nls.append(m.id)
# print(nls)

# if not nls:
#     print('Helo')

check = Moviedata.query.get(1)
print(check)

# ls = []
# ls.append(check.title)
# ls.append(check.id)
# ls.append(check.poster_path)
# print(ls)

new_wl = []

def ml():
    wl = Moviedata.query.all()
    for w in wl:
        new_wl.append(w.title)
    return new_wl
print(ml())