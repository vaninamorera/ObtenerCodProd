import pandas as pd

base_import = 'C:/Users/Vanin/Documents/descripABB.xlsx'
base = pd.read_excel(base_import)

#base['Modelo1'] = base['Modelo'].str.extract(r'.*CODIGO:\s(\S*)') 
#extrae carácteres que no contengan espacios (palabras o cód complet@s) luego de "CODIGO:" 
#base['Modelo1'] = base['Modelo'].str.replace('-','') #quita los guiones de la columna y los reemplaza por espacio
base['Modelo1'] = base['Modelo'].str.extract(r'.*PARTE:\s(\S*)') 

base.to_excel('C:/Users/Vanin/Documents/descripABB.xlsx')

print(base)
