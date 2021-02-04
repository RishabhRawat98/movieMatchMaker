import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


lst_titles = ['Moonlight', 'The Artist', 'Spotlight']
def clean_Engine(lst_titles):
    unclean_data = pd.read_csv('Moviedb.csv') #There is a problme withe the csv, genreates unnmed: 0 column
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
    final_reco()

    # fin_ls = []
    # def final_id():
    #     for i in range(len(rec_tit)):
    #         mov_id = movdb[movdb.title == rec_tit[i]]['Movlst_id'].values[0]
    #         fin_ls.append(mov_id)
    # return fin_ls

    # print(final_id())
    # print(fin_ls)
    return rec_tit


print(clean_Engine(lst_titles))