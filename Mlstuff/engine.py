import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

unclean_data = pd.read_csv('new.csv') #There is a problme withe the csv, genreates unnmed: 0 column
unclean_data.rename( columns={'Unnamed: 0':'Movlst_id'}, inplace=True ) #This renames the unnamed: 0 column to somethig more useful

genre_columns = ['title', 'genre1', 'genre2', 'genre3', 'genre4']
# unclean_data[genre_columns].isnull().any() #This tells you this is unclean data, and we knew that just looking at it Uncomment this command to see, use jupyter idk how vscode would look like

clean_data = unclean_data.fillna(0)#This replaces the Nan fields as 0
# clean_data[genre_columns].isnull().any() #check if the data is now cleaned, it is now clean. Again i did thsi on jupyyter so no clue how it looks on vs, best to leave this line be


#Function to combine the attributes of a film we want to compare
def combiner(data):
    mov_combat = []
    for i in range(0, data.shape[0]):
        mov_combat.append(data['title'][i]+' '+str(data['genre1'][i])+' '+str(data['genre2'][i])
                          +' '+str(data['genre3'][i])+' '+str(data['genre4'][i]))
    return mov_combat

movdb = clean_data.drop('gnere5', axis=1) #Column not needed
movdb['combat'] = combiner(clean_data) #This makes a new column with the combined attributes from the function above

cm = CountVectorizer().fit_transform(movdb['combat']) #Turns values in the combat column into vecotrs. Now we can do math 
cs = cosine_similarity(cm) #This gives us the table of each movie with a rating of simiilarity to each other film
# cs.shape            'Uncomment to get the size of the array requrend by cosine similartiy, each movie is compared to each other. 


lst_titles = ['Moonlight', 'Green Book', 'Wings'] # IMPORTANT!!!!! This is userwatch list, connect this line to sql somehow.
new_n = []
def id_getter():
    
    for mindex, mtitle in enumerate(lst_titles):
        get_movid = movdb[movdb.title == mtitle]['Movlst_id'].values[0]
        new_n.append(get_movid)
    return new_n
# print(id_getter()) #This function is returning the ids of each film in the users watch list

def lets_work():
    emp = []
    for num in new_n:
        sc = list(enumerate(cs[num]))
        emp.append(num)
        emp.append(sc)
        
    return emp
#Basically this function return a list with the id of the film and the unsorted_recommendation list.  The format is emp = [ id, [(0, 0.101), (1, 0.832), (2, 0.43)....] , id2 , [(0, 0.9999999999999999, )...]   ]

