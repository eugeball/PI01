from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import pandas as pd
from limpieza import df_completo
import requests


app = FastAPI()
deta = Deta("e0euqexa_fKMRASEhZhw2NEhEHwragyYucsZCajkF")  # configure your Deta project 
drive = deta.Drive("images") # access to your drive

@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Individual N°1 - Data Engineering Henry</title>
</head>
<style>
  body {  background-color: FAEBD7;
          font-family: monospace;
          font-size: 60%;}
  h1   {  color: C71585;
          font-family: family;
          font-size: 150%;}
  h3   {  color:BC8F8F;
          font-family: verdana;
          font-size: 150%;}
  p    {  color: D87093;
          font-family: verdana;
          font-size: 200%;}
  
</style>
<body>
    <h1><p style="border: ridge #BC8F8F 1px;">Guia de Usuario                 by Eugenia Ball.</h1></p>

    <h3>Importante: Los textos ponerlos entre las barras ej: /netflix/love </h3>
    <p> · Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma:</p>
    <h3>Ej: /get_word_count/netflix/love</h3> 
    <p> · Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año:</p>
    <h3>Ej: /get_score_count/netflix/85/2010</h3>
    <p> · La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos:</p>
    <h3>Ej: /get_second_score/amazon</h3>
    <p> · Pelicula que más duro según año , plataforma y tipo de duración:</p>
    <h3>Ej: /get_longest/netflix/min/2016</h3>
    <p> · Cantidad de series y películas por rating:</p>
    <h3>Ej: /get_rating_count/18+</h3>
    <p>Luego de realizar alguna consulta, si desea volver a esta guía, elimine las barras.</p>
</body>
</html>"""



# Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma
@app.get("/get_word_count/{plataforma}/{keyword}") # get_word_count/netflix/love
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
@app.get("/get_score_count/{plataforma}/{point}/{anio}") #get_score_count/netflix/85/2010
def get_score_count(plataforma:str,point:int,anio:int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
    df_temp = df_completo[(df_completo["score"]>point)&(df_completo["release_year"]==anio)&(df_completo.id.str[0] == dicc[plataforma])&(df_completo["type"] == "movie")]
    data = df_temp.groupby(df_temp.id.str[0]).count().iloc[:,0]
    data = data.rename_axis("Cantidad").rename({v: k for k, v in dicc.items()})
    return data.to_dict()
    
    

# La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/get_second_score/{plataforma}")   # get_second_score/amazon
def get_second_score(plataforma):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == dicc[plataforma])&(df_completo['type'] == 'movie')].sort_values(["score","title"],ascending=[False,True]).reset_index(drop=True)
    titulo = df_temp.iloc[1,2]
    score = df_temp.iloc[1,14]
    return f' La segunda pelicula es {titulo} , con un puntaje de {score}'



# pelicula que mas duro segun año , plataforma y tipo de duracion
@app.get("/get_longest/{plataforma}/{duration_tipo}/{date}") #get_longest/netflix/min/2016
def get_longest(plataforma:str,duration_tipo:str,date:int):
    plataformas = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_completo[(df_completo['id'].str[0] == plataformas[plataforma])&(df_completo['release_year']==date)&(df_completo['duration_type']==duration_tipo)&\
          (df_completo['type']=='movie')].sort_values(['duration_int'], ascending=False).reset_index(drop=True)[["title","duration_int","duration_type"]].iloc[0,:]
  
    return df_temp.to_dict()
 

 # Cantidad de series y películas por rating
@app.get("/get_rating_count/{rating}") # /get_rating_count/18+
def get_rating_count(rating):
    
    cantidad_rating= df_completo[df_completo['rating']== rating]

    return f' Existen {len(cantidad_rating)} peliculas/series , con rating {rating}'