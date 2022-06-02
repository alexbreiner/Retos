import pandas as pd
#import csv 
# ruta file csv
rutaFileCsv ='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv) -> str:
    if rutaFileCsv != 'csv':
        try:
            movies = pd.read_csv(rutaFileCsv)
            
            #mostrar el subconjunto mediante dataFrame
            df = pd.DataFrame(movies, columns = ['Country', 'Language', 'Gross Earnings'])
            print(df)
            #Mostrar lista de cuidades
            pivote = df.pivot_table(index = ['Country', 'Language'], values = ['Gross Earnings'])
            
            #Validar que solo sean 10 registros
            return pivote.head(10)
        
        except:
            return 'Error al leer el archivo de datos.'
    else:
        return 'Extensión invalida.'
    
lista = listaPeliculas(rutaFileCsv)
print(lista)
