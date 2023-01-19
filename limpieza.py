#IMPORTO LO QUE VOY A USAR
import pandas as pd

#EMPIEZO CON LAS TRANSFORMACIONES
url_amazon = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/amazon_prime_titles-score.csv'
amazon_titles = pd.read_csv(url_amazon)
url_disney= 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/disney_plus_titles-score.csv'
disney_plus_titles = pd.read_csv(url_disney)
url_hulu = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/hulu_titles-score%20(2)%20copy.csv'
hulu_titles = pd.read_csv(url_hulu)
url_netflix = 'https://raw.githubusercontent.com/lucasrdrz/PI-01/main/netflix_titles-score.csv'
netflix_titles = pd.read_csv(url_netflix)

#arreglo el tipo de datos
# amazon_titles
amazon_titles['show_id'] = amazon_titles['show_id'].astype('str')
amazon_titles['type'] = amazon_titles['type'].astype('category')
amazon_titles['title'] = amazon_titles['title'].astype('str')
amazon_titles['director'] = amazon_titles['director'].astype('str')
amazon_titles['cast'] = amazon_titles['cast'].astype('str')
amazon_titles['country'] = amazon_titles['country'].astype('str')
amazon_titles['date_added'] = pd.to_datetime(amazon_titles['date_added'], infer_datetime_format=True, errors='coerce')
amazon_titles['release_year'] = amazon_titles['release_year'].astype('int16')
amazon_titles['rating'] = amazon_titles['rating'].astype('str')
amazon_titles['listed_in'] = amazon_titles['listed_in'].astype('str')
amazon_titles['description'] = amazon_titles['description'].astype('str')
amazon_titles['score'] = amazon_titles['score'].astype('int8')

# disney_plus_titles
disney_plus_titles['show_id'] = disney_plus_titles['show_id'].astype('str')
disney_plus_titles['type'] = disney_plus_titles['type'].astype('category')
disney_plus_titles['title'] = disney_plus_titles['title'].astype('str')
disney_plus_titles['director'] = disney_plus_titles['director'].astype('str')
disney_plus_titles['cast'] = disney_plus_titles['cast'].astype('str')
disney_plus_titles['country'] = disney_plus_titles['country'].astype('str')
disney_plus_titles['date_added'] = pd.to_datetime(disney_plus_titles['date_added'], infer_datetime_format=True, errors='coerce')
disney_plus_titles['release_year'] = disney_plus_titles['release_year'].astype('int16')
disney_plus_titles['rating'] = disney_plus_titles['rating'].astype('str')
disney_plus_titles['listed_in'] = disney_plus_titles['listed_in'].astype('str')
disney_plus_titles['description'] = disney_plus_titles['description'].astype('str')
disney_plus_titles['score'] = disney_plus_titles['score'].astype('int8')

# hulu_titles
hulu_titles['show_id'] = hulu_titles['show_id'].astype('str')
hulu_titles['type'] = hulu_titles['type'].astype('category')
hulu_titles['title'] = hulu_titles['title'].astype('str')
hulu_titles['director'] = hulu_titles['director'].astype('str')
hulu_titles['cast'] = hulu_titles['cast'].astype('str')
hulu_titles['country'] = hulu_titles['country'].astype('str')
hulu_titles['date_added'] = pd.to_datetime(hulu_titles['date_added'], infer_datetime_format=True, errors='coerce')
hulu_titles['release_year'] = hulu_titles['release_year'].astype('int16')
hulu_titles['rating'] = hulu_titles['rating'].astype('str')
hulu_titles['listed_in'] = hulu_titles['listed_in'].astype('str')
hulu_titles['description'] = hulu_titles['description'].astype('str')
hulu_titles['score'] = hulu_titles['score'].astype('int8')

# netflix_title
netflix_titles['show_id'] = netflix_titles['show_id'].astype('str')
netflix_titles['type'] = netflix_titles['type'].astype('category')
netflix_titles['title'] = netflix_titles['title'].astype('str')
netflix_titles['director'] = netflix_titles['director'].astype('str')
netflix_titles['cast'] = netflix_titles['cast'].astype('str')
netflix_titles['country'] = netflix_titles['country'].astype('str')
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'], infer_datetime_format=True, errors='coerce')
netflix_titles['release_year'] = netflix_titles['release_year'].astype('int16')
netflix_titles['rating'] = netflix_titles['rating'].astype('str')
netflix_titles['listed_in'] = netflix_titles['listed_in'].astype('str')
netflix_titles['description'] = netflix_titles['description'].astype('str')
netflix_titles['score'] = netflix_titles['score'].astype('int8')

#Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma,
#seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
amazon_titles['id'] = 'a' + amazon_titles['show_id']
amazon_titles['id'] = amazon_titles['id'].astype('str')
disney_plus_titles['id'] = 'd' + disney_plus_titles['show_id']
disney_plus_titles['id'] = disney_plus_titles['id'].astype('str')
hulu_titles['id'] = 'h' + hulu_titles['show_id']
hulu_titles['id'] = hulu_titles['id'].astype('str')
netflix_titles['id'] = 'n' + netflix_titles['show_id']
netflix_titles['id'] = netflix_titles['id'].astype('str')

## Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”
amazon_titles.fillna({'rating': 'g'}, inplace=True) #amazon['rating'].fillna("G", inplace= True)
disney_plus_titles.fillna({'rating': 'g'}, inplace=True)
hulu_titles.fillna({'rating': 'g'}, inplace=True)
netflix_titles.fillna({'rating': 'g'}, inplace=True)

##  De haber fechas, deberán tener el formato **`AAAA-mm-dd`**
amazon_titles['date_added'] = pd.to_datetime(amazon_titles['date_added'], infer_datetime_format=True, errors='coerce')
disney_plus_titles['date_added'] = pd.to_datetime(disney_plus_titles['date_added'], infer_datetime_format=True, errors='coerce')
hulu_titles['date_added'] = pd.to_datetime(hulu_titles['date_added'], infer_datetime_format=True, errors='coerce')
netflix_titles['date_added'] = pd.to_datetime(netflix_titles['date_added'], infer_datetime_format=True, errors='coerce')

# El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**.
# El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
amazon_titles[['duration_int', 'duration_type']] = amazon_titles['duration'].str.split(' ', n=-1, expand=True, regex=None)
amazon_titles = amazon_titles[amazon_titles.columns[:10].tolist() + ['duration_int', 'duration_type'] + amazon_titles.columns[10:-2].tolist()]
disney_plus_titles[['duration_int', 'duration_type']] = disney_plus_titles['duration'].str.split(' ', n=-1, expand=True, regex=None)
disney_plus_titles = disney_plus_titles[disney_plus_titles.columns[:10].tolist() + ['duration_int', 'duration_type'] + disney_plus_titles.columns[10:-2].tolist()]
hulu_titles[['duration_int', 'duration_type']] = hulu_titles['duration'].str.split(' ', n=-1, expand=True, regex=None)
hulu_titles = hulu_titles[hulu_titles.columns[:10].tolist() + ['duration_int', 'duration_type'] + hulu_titles.columns[10:-2].tolist()]
netflix_titles[['duration_int', 'duration_type']] = netflix_titles['duration'].str.split(' ', n=-1, expand=True, regex=None)
netflix_titles = netflix_titles[netflix_titles.columns[:10].tolist() + ['duration_int', 'duration_type'] + netflix_titles.columns[10:-2].tolist()]

#cambio seasons por season
amazon_titles['duration_type'] = amazon_titles['duration_type'].replace('Seasons' , 'season')
disney_plus_titles['duration_type'] = disney_plus_titles['duration_type'].replace('Seasons' , 'season')
hulu_titles['duration_type'] = hulu_titles['duration_type'].replace('Seasons' , 'season')
netflix_titles['duration_type'] = netflix_titles['duration_type'].replace('Seasons' , 'season')

#uno las tablas a un df completo
df_completo= pd.concat([netflix_titles,hulu_titles,disney_plus_titles,amazon_titles])

#aca pongo todo en minusculas
df_completo['id'] = df_completo['id'].str.lower()
df_completo['type'] = df_completo['type'].str.lower()
df_completo['title'] = df_completo['title'].str.lower()
df_completo['director'] = df_completo['director'].str.lower()
df_completo['cast'] = df_completo['cast'].str.lower()
df_completo['country'] = df_completo['country'].str.lower()
df_completo['rating'] = df_completo['rating'].str.lower()
df_completo['listed_in'] = df_completo['listed_in'].str.lower()
df_completo['description'] = df_completo['description'].str.lower()
df_completo['duration_type'] = df_completo['duration_type'].str.lower()

df_completo.duration_int=df_completo.duration_int.fillna(0)
df_completo.duration_int=df_completo['duration_int'].astype(int)
df_completo

# Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma
# get_word_count/netflix/love
def get_word_count(plataforma , keyword):
    cantidad_de_keyword=df_completo.loc[df_completo['title'].str.contains (keyword )]
    tabla_id = cantidad_de_keyword.groupby(['id']).size().reset_index(name='cantidad de id')
    lista=list(plataforma)
    if lista[0] == 'a':
        plataforma = 'amazon'
        cantidad_a = tabla_id['id'].str.startswith('a').sum()
        return plataforma, cantidad_a , f'En la plataforma {plataforma} , aparece la palabra ingresada {cantidad_a} de veces  '
    else:
        pass
    if lista[0] == 'd':
        plataforma = 'disney'
        cantidad_d = tabla_id['id'].str.startswith('d').sum()
        return plataforma, cantidad_d , f'En la plataforma {plataforma} ,aparece la palabra ingresada {cantidad_d} de veces '
    else:
        pass
    if lista[0] == 'h':
        plataforma = 'hulu'
        cantidad_h = tabla_id['id'].str.startswith('h').sum()
        return plataforma, cantidad_h , f'En la plataforma {plataforma} , aparece la palabra ingresada {cantidad_h} de veces '
    else:
        pass

    if lista[0] == 'n':
        plataforma = 'netflix'
        cantidad_n = tabla_id['id'].str.startswith('n').sum()
        return  f'En la plataforma {plataforma} , aparece la palabra ingresada {cantidad_n} de veces '   
    else:
        return f' Error '


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
#get_score_count/netflix/85/2010
def get_score_count(plataforma:str,point:int,anio:int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
    df_temp = df_completo[(df_completo["score"]>point)&(df_completo["release_year"]==anio)&(df_completo.id.str[0] == dicc[plataforma])&(df_completo["type"] == "movie")]
    data = df_temp.groupby(df_temp.id.str[0]).count().iloc[:,0]
    data = data.rename_axis("Cantidad").rename({v: k for k, v in dicc.items()})
    return data.to_dict()
    
    

# La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos.
# get_second_score/amazon
def get_second_score(plataforma):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == dicc[plataforma])&(df_completo['type'] == 'movie')].sort_values(["score","title"],ascending=[False,True]).reset_index(drop=True)
    titulo = df_temp.iloc[1,2]
    score = df_temp.iloc[1,14]
    return f' La segunda pelicula es {titulo} , con un puntaje de {score}'



# pelicula que mas duro segun año , plataforma y tipo de duracion
#get_longest/netflix/min/2016
def get_longest(plataforma:str,duration_tipo:str,date:int):
    plataformas = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == plataformas[plataforma])&(df_completo['release_year']==date)&(df_completo['duration_type']==duration_tipo)&\
          (df_completo['type']=='movie')].sort_values(['duration_int'], ascending=False).reset_index(drop=True)[["title","duration_int","duration_type"]].iloc[0,:]
  
    return df_temp.to_dict()
 

# Cantidad de series y películas por rating
# /get_rating_count/18+
def get_rating_count(rating):
    
    cantidad_rating= df_completo[df_completo['rating']== rating]

    return f' Existen {len(cantidad_rating)} peliculas/series , con rating {rating}'