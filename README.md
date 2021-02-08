# Movie Matchmaker project

[![License: MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](https://opensource.org/licenses/MIT)

![](flaskblog/static/Movie-Matchmaker-demo.gif)

Movie Matchmaker is an app that allows users to create an account and like or dislike movie cards from a database. Users can afterwards see a list of their liked and disliked movies,  as well as a list of recommended movies based on their preferences

## Installation & Usage

### Installation

* Fork and clone or download the repo.
* Open terminal
* Run `pipenv install` to install dependencies.
* Run `pipenv shell` to open virtual environment.
* Run `export FLASK_APP=run.py` to tell terminal which application to work with (Linux/MacOS/GitBash).
* Run `export FLASK_ENV=development` to tell terminal which environment to work in (Linux/MacOS/GitBash).

### Usage

* Run `flask run` to launch the flask application.

## Usage 

* Go to the welcome page and click the 'Sign Up' button.

* Enter your details and press 'Submit'. You will be redirected to the 'Login' page.

* Type in the email and password you used to sign up.

* On the Swipe page click the "Yes" or "No" buttons depending on whether you like the currently displayed movie or not.


## Technologies

* Figma
* HTML
* CSS
* Bootstrap
* Python
* Flask
* SQLite
* Pytest



## Process

The project started with deciding what the topic and aim of our application would be. This was followed by sketching a rough design and plan using Figma. We then allocated a time frame for each task outlined and logged our progress and remaining tasks.

After the planning and designing step, we worked individually on separate tasks. After completing our individual work, we worked together by mob programming to try and connect them. We used the remaining time to implement testing for both sides and correct bugs and add fixes.

Everytime a new functioning feature was completed, its branch was merged to the Development branch and pushed to the main git repository. At the end all final changes were merged with the master branch.

## Code Snippets

The machine learning function called clean engine.

```Python
def clean_Engine(lst_titles):
    unclean_data = pd.read_csv('D:\\AuthWorking\\06-Login-Auth\\flaskblog\\Moviedb.csv') #There is a problme withe the csv, genreates unnmed: 0 column
    unclean_data.rename( columns={'Unnamed: 0':'Movlst_id'}, inplace=True )

    genre_columns = ['title', 'genre1', 'genre2', 'genre3', 'genre4']
    clean_data = unclean_data.fillna(0)


    def combiner(data):
        mov_combat = []
        for i in range(0, data.shape[0]):
            mov_combat.append(data['title'][i]+' '+str(data['genre1'][i])+' '+str(data['genre2'][i])
                          +' '+str(data['genre3'][i])+' '+str(data['genre4'][i]))
        return mov_combat

    movdb = clean_data.drop('gnere5', axis=1) #Column not needed
    movdb['combat'] = combiner(clean_data)

    cm = CountVectorizer().fit_transform(movdb['combat']) #Turns values in the combat column into vecotrs. Now we can do math 
    cs = cosine_similarity(cm)

    new_n = []
    def id_getter():
        for mindex, mtitle in enumerate(lst_titles):
            get_movid = movdb[movdb.title == mtitle]['Movlst_id'].values[0]
            new_n.append(get_movid)
        return new_n
    
    id_getter()

    emp = []
    def lets_work():
        for num in new_n:
            sc = list(enumerate(cs[num])) 
            emp.append(sc)
        
        return emp
    lets_work()

    kuro = []
    def get_kuro():
        for i in range(len(emp)):
            list1,list2 = zip(*emp[i])
            kuro.append(list2)
        return kuro
    get_kuro()

    shiro = pd.DataFrame(kuro[1])
    def get_shiro():
        for i in range(len(kuro)):
            shiro['col{}'.format(i)] = pd.DataFrame(kuro[i])
        return shiro

    (get_shiro())

    yoo_shiro = shiro.drop(0,axis=1) #dropping a useless column
    yoo_shiro['mean'] = yoo_shiro.mean(axis=1)
    eh_shiro = pd.DataFrame(yoo_shiro['mean']) #new dataframe with the only column as mean of the pervious columns
    eh_shiro['id'] = eh_shiro.index #creates a new column and gives each movie an id

    records = eh_shiro.to_records(index=False) 
    result = list(records)
    sorted_for_life = sorted(result, key = lambda x:x [0], reverse = True) #Uses the built in mergesort algo, sorts form index 0 which is the mean recomended socre.

    rec_tit = []
    def final_reco():
        j = 0

        for item in sorted_for_life:
            movie_title = movdb[movdb.Movlst_id == item[1]]['title'].values[0]
            if movie_title in lst_titles:
                continue
            else:
                rec_tit.append(movie_title)
                j = j + 1
                if j > 15:
                    break
        return rec_tit
```

## Wins & Challenges

Wins | Challenges
------------ | -------------
Improved understanding of designing apps with Flask. | Cleaning data for the machine learning algorithm.
Successfully set up a machine learning algorithm. | Inserting data from CSV files into SQL databases.
Succesful implementation of authentication and authorisation. | Achieving a high coverage with the pytest testing.
Inserted an animation in the footer. | Displaying the recommended movies list.

## Features

* Ability to sign up and login to the app.
* Ability to predict user's taste in movies with the machinelearning algorithm.
* Ability to save liked and disliked movies in the database.

## Future Features

* A more visually-appealing styling.
* Responsive design for mobile users.
* Having a list of already watched movies.
* Redirecting users to movie trailers.

## Licence

* [MIT Licence](https://opensource.org/licenses/mit-license.php)

To visit the site click this link (coming soon).