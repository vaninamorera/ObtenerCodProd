import pandas as pd

base_import = 'C:/Users/Vanin/Documents/descripABB.xlsx'
base = pd.read_excel(base_import)

#base['Modelo1'] = base['Modelo'].str.extract(r'.*CODIGO:\s(\S*)') #extrae carácteres que no contengan espacios (palabras o cód complet@s) luego de los dos puntos 
#base['Modelo1'] = base['Modelo'].str.replace('-','') #quita en el string de la columna los guiones
base['Modelo1'] = base['Modelo'].str.extract(r'.*PARTE:\s(\S*)')

base.to_excel('C:/Users/Vanin/Documents/descripABB.xlsx')

print(base)
