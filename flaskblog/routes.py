from flask import render_template, url_for, flash, redirect, request, session, jsonify
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, UserWatchlist, DontWatchlist, RecomendedList, Moviedata
from flask_login import login_user, current_user, logout_user, login_required
import random
from flaskblog.cleanengine import clean_Engine
a = None
b = None
rec_ls = []
new_wl = []
close_lst = []
watch_count = 0
def ml_Input():
        wl = UserWatchlist.query.all()
        for w in wl:
            new_wl.append(w.title)

        return new_wl

def w_counter(data):
    if watch_count == 1 or watch_count%5 == 0: 
        watch_count + 1
        return clean_Engine(data), watch_count
    else:
        return watch_count + 1
@app.route("/home")
def home():
    allRec = RecomendedList.query.all()              # This queries recomended list table for all values
    for i in allRec:
        rec_ls.append(i.title)
    if not rec_ls:
        print('IFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')
        x = random.randint(0,90)
        realMovInfo = Moviedata.query.get(x)
        # return realMovInfo
    else:
        print('ELSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        mov_title = rec_ls[0]
        print(mov_title)
        realMovInfo = Moviedata.query.filter_by(title = mov_title).first()
        print(realMovInfo, 'WHaterver-----------------------------------------------')
        # return realMovInfo

        
    mov_dic = {                                                         # This dicitonary will be used to render the movieinfo.
            "id": realMovInfo.id,
            "title": realMovInfo.title,
            "poster": realMovInfo.poster_path,
            "rel": realMovInfo.release_date,
            "desc": realMovInfo.overview,
            "genre": realMovInfo.genre1,
        } 
    global a,b
    a = realMovInfo.title
    b= realMovInfo.id    
    return render_template('home.html', name=current_user.username,  
                                        movieTitle=mov_dic['title'], 
                                        movieImgURL=mov_dic['poster'], 
                                        movieReleaseDate=mov_dic['rel'], 
                                        movieBrief=mov_dic['desc'])
    
def addToWatch():
    global a,b
    add_mov = UserWatchlist(user_id = current_user.username, title = a, movie_id = b) #UPTO HERE THE CODE IS WOKRING
    db.session.add(add_mov)
    db.session.commit()
    titles_rec = w_counter(ml_Input())
    for item in titles_rec:
        close_lst.append(item)

    print(close_lst)
    for i in close_lst[0]:
        new_entry = RecomendedList(user_id = current_user.username, title = i) 
        print(new_entry)
        db.session.add(new_entry)
        db.session.commit()
    
    delid = RecomendedList.query.first()
    print(delid)
    db.session.delete(delid)
    db.session.commit()
    # return close_lst

    #above function is bad it locks the database.

#The database is locked by another process that is writing to it. You have to wait until the other transaction is committed. See the documentation of connect()


@app.route("/home", methods=['POST'])
def button():
    if request.form['bro_button'] == 'no':
        print('no')
    elif request.form['bro_button'] == 'yes':
        addToWatch()
        print(rec_ls, 'wWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
        del rec_ls[0]
        print(close_lst)
    return home()       #this is to test the data, if this is no, no recomended list

# lst = []
# mov_list = UserWatchlist.query.all()
# for mov in mov_list:
#     mov_id = mov.id
#     lst.append(mov_id)

# mov_list2 = [{"title":"Argos"}]
# for i in lst:
#     mov_query = Moviedata.query.get(id = lst[i])
#     mov_list2.append(mov_query)
    
@app.route("/about")
def mov_get():
    allRec = RecomendedList.query.all()
    for i in allRec:
        rec_ls.append(i.id)
    if not rec_ls:
        return jsonify(close_lst)
    else: 
        return render_template('about.html', liked_movies_list=["Argos"])
    # return render_template('about.html', liked_movies_list=["Argos"])


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')





#########################################################
    #Yes function 


# ml_Input()


#     #need some sort of add envent listener, to listen to yes button
# def addToWatch():
#     add_mov = UserWatchList(user_id = current_user.username, movie_id = mov_dic['id'], title = mov_dic['title'] )
#     delid = RecomendedList.query.all(1)
#     db.session.add(add_mov)
#     del_rec = RecomendedList.query.filter_by(id = delid.id).delete()
#     db.session.commit()
#     w_counter(ml_Input())
    
############################################################################



# 