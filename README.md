# PI01
Proyecto Individual 01.

## Introducción:

Mi nombre es Eugenia Ball, al momento de hacer este proyecto me encuentro cursando la etapa de Labs para la carrera de Data Science de SoyHenry.

En este proyecto vamos a realizar el trabajo de Data Engineer. Para ello se nos entregan 4 datasets de distintas plataformas de streaming (Amazon, Disney, Hulu y Netflix) y debemos realizar un Análisis Exploratorio de Datos sobre cada uno y corregir imperfecciones como diferencias en el tipo de los datos, valores nulos,  etc.

## Explicación del Proyecto :

Realice un trabajo de ETL sobre los conjuntos de datos recibidos y desarrolle una API con FastApi para disponibilizar los datos. El deployment de la API se realizo en Deta.

Las consultas a realizar son:

· Cantidad de veces que aparece una palabra clave en el título de peliculas/series, por plataforma.

· Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

· La segunda película con mayor partitura para una plataforma determinada, según el orden alfabético de los títulos.

· Película que más apareció según año, plataforma y tipo de duración.

· Cantidad de series y películas por rating.

## Explicación de los contenidos del Repositorio:

En la carpeta proyecto se encuentra:

· Los datasets analizados.

· El archivo main.py que es el archivo en el cual se configura FastAPI y se instancian los decoradores de la API .

· El archivo limpieza.py en el cual se encuentra todo el proceso de Etl comentado.

· El archivo request.

## Herramientas usadas:

· FastApi.

· Deta.

· Python.

· Pandas.

· Requests.

## Adicional:

· Video de muestra :

https://youtu.be/t_X4w5ctnXg

· Guia de usuario de la Api:

https://rmwpeq.deta.dev/

· Enlaces de prueba :

https://rmwpeq.deta.dev/get_word_count/netflix/love

https://rmwpeq.deta.dev/get_score_count/netflix/85/2010

https://rmwpeq.deta.dev/get_second_score/amazon

https://rmwpeq.deta.dev/get_longest/netflix/min/2016

https://rmwpeq.deta.dev/get_rating_count/18+    
