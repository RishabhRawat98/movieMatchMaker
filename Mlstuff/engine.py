import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

unclean_data = pd.read_csv('Moviedb.csv') #There is a problme withe the csv, genreates unnmed: 0 column
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
id_getter()
# print(id_getter()) #This function is returning the ids of each film in the users watch list
emp = []
def lets_work():
    
    for num in new_n:
        sc = list(enumerate(cs[num]))
        # emp.append(num)    This line is more hassle then its worth, 
        emp.append(sc)
        
    return emp
lets_work()
#The format of emp is [[(0, 0.3), (1, 0.43), (2, 0.11)], [(0, 0.144), (1, 0.22), (2, 0.71)],  [(0, 0.44), (1, 0.62), (2, 0.41)]]]
#So there is a list emp which contains 3 more lists, and inside each list is 92 tuples. 
#How we extract tuples.....

#This function is unpacking the tuples, and then adding the list of individual scors into the empty list kuro
kuro = []
for i in range(len(emp)):
    list1,list2 = zip(*emp[i])
    kuro.append(list2)

#This function is createing a df wiht dynamic naming, so basically, a new column is created with the name coli where i is a number,
#
shiro = pd.DataFrame(kuro[1])
for i in range(len(kuro)):
    shiro['col{}'.format(i)] = pd.DataFrame(kuro[i])

yoo_shiro = shiro.drop(0,axis=1) #dropping a useless column
yoo_shiro['mean'] = yoo_shiro.mean(axis=1)
eh_shiro = pd.DataFrame(yoo_shiro['mean']) #new dataframe with the only column as mean of the pervious columns
eh_shiro['id'] = eh_shiro.index #creates a new column and gives each movie an id

records = eh_shiro.to_records(index=False) #This makes a tuple of the mean and the movie id [(0.50540926,  0) (0.25811793,  1) ...]going all the way upto 99
# print(records) #uncomment to see how the data looks
result = list(records)
# print(result)
sorted_for_life = sorted(result, key = lambda x:x [0], reverse = True) #Uses the built in mergesort algo, sorts form index 0 which is the mean recomended socre.
# print(sorted_for_life)


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

final_reco()
print(rec_tit) #cannot print the actual function, because callign the function twice will and to the list twice giving the same reseult but reapeated. Good find. 


fin_ls = []
def final_id():
    for i in range(len(rec_tit)):
        mov_id = movdb[movdb.title == rec_tit[i]]['Movlst_id'].values[0]
        fin_ls.append(mov_id)
    return fin_ls

final_id()
print(fin_ls) #See above for rec_tit