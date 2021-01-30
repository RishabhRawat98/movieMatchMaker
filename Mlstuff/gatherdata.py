import pandas as pd
import numpy as np
target = pd.read_json(
    'https://api.themoviedb.org/3/list/28?api_key=bf72f36bd4b5c9bc241aafbecc423728&language=en-UK') #this is getting the json data from themoviedb api 



burner_df = pd.DataFrame(target['items'].tolist()) #The original json is nested, this goes into the the items section and gets the data from there

fields = ['video', 'vote_average', 'vote_count', 'original_language', 'adult',
          'backdrop_path', 'media_type', 'original_title', 'id', 'genre_ids' ]

almostdb = burner_df.drop(fields, axis=1) #this is the burner df without the fields listed above, cleans up the data and makes it usable

#This function gets the movie genres which are nested within the gnree_ids which is nested in items
film_genres = []
for i in target['items']:
    film_genres.append(i['genre_ids'])

genredb = pd.DataFrame(film_genres, columns = ['genre1', 'genre2', 'genre3', 'genre4', 'gnere5'])

resultdb = pd.concat([almostdb, genredb], axis=1, join="inner")
resultdb.to_csv('Moviedb')
# print(resultdb)