import random
from cleanengine import clean_Engine
from .sec import MovieData


@app.route('/')                                                           #you want try/except because initally the user has no Recomended list
def homepage():
    try:
        checkRecList = UserRecList.query.all(1)                           #This basically should add id from the recomended list t
        mov_id = checkRecList.movie_id
        realMovInfo = Moviedata.query.get(mov_id)                         #This uses the movie id to get the movie from Moviedata
        mov_dic = {                                                       #This dicitonary will be used to render the movieinfo
            id = realMovInfo.id
            title = realMovInfo.title
            poster = realMovInfo.poster_path
            rel = realMovInfo.release_date
            desc = realMovInfo.description
            genre = realMovInfo.genre1
        }
    except NameError:
        x = random.randint(0,90)
        realMovInfo = Moviedata.query.get(x)
        mov_dic = {
            id = realMovInfo.id
            title = realMovInfo.title
            poster = realMovInfo.poster_path
            rel = realMovInfo.release_date
            desc = realMovInfo.description
            genre = realMovInfo.genre1

    #Add the html stuff here 
    # return render_template                          This is how the function shoudl end sorta.




    #Yes function 
    def addToWatch():
        add_mov = UserWatchList(user_id = user.current, movie_id = mov_dic['id'] )
        delid = UserRecList.query.all(1)
        del_rec = UserRecList.query.filter_by(id = delid.id).delete()
        db.session.add(add_mov)
        db.session.commit()

        ##Run the ML function 
        #Prolly reload the page or something/?????
    

    #No Fucntion
    def dontLike():
        add_mov = DontLikeList(user_id = user.current, movie_id = mov_dic['id'] )
        delid = UserRecList.query.all(1)
        del_rec = UserRecList.query.filter_by(id = delid.id).delete()
        db.session.add(add_mov)
        db.session.commit()

        #Again realod the page to show the next recommendation

######
#For cleanEngine() need a sql query of the UserWatch list
def ml_Input():
    wl = UserWatchList.query.all()
    new_wl = []
        for w in wl:
            new_wl.append(wl.title)

    return new_wl
#Now you can run cleanEngine(ml_Input)
#The output of clean engine.py is a list, now can be used ot make a new db table
#Make the recomendation table which is user id and movie id/title
