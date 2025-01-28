# Filtrado de datos
import pandas as pd

oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'])
print(oceans)
# Atributo index
print(oceans.index)
print(type(oceans.index))
print('\nIndice personalizado')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'])
oceans.index = [1, 2, 3, 4, 5]
print(oceans)
print(oceans.index)
print(type(oceans.index))
print('\nOtra forma de estableces indices')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'],
                   index=[1, 2, 3, 4, 5])
print(oceans)
print(oceans.index)
print(type(oceans.index))
print('\nIndices como cadenas')
oceans = pd.Series(['Pacific', 'Atlantic', 'Indian', 'Southern', 'Artic'],
                   index=['A', 'B', 'C', 'D', 'E'])
print(oceans)
print(oceans.index)
print(type(oceans.index))


print('\nIndexación mediante loc[]\n')
states = ['Alabma', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camelia', 'Foget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-Spotted skimmer dragonfly', 'Two-tailed swallowtail', 'Europen honey bee']
index = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
print(df)
print('\nArkansas insect is:')
print(df.loc['state 4', 'insect'])
print(df.loc['state 1':'state 3','flower'])
print(df.loc['state 1':'state 3', 'flower':'insect'])

print('\nIndexación mediante iloc[]')
print(df.iloc[3,2])
print(df.iloc[[0,2],1:])

print('\nIndexación negativa con iloc[]')
print(df.iloc[[0,2], -1])

print('\nMétodo set_index()')
states = ['Alabma', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camelia', 'Foget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-Spotted skimmer dragonfly', 'Two-tailed swallowtail', 'Europen honey bee']
index = ['state 1', 'state 2', 'state 3', 'state 4']
print('DataFrame Original')
df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
print(df)
print('DataFrame con nuevo indice')
df = df.set_index('state')
print(df)
print()
print(df.index)

print('\nEliminando el nombre del indice')
df.index.name = None
print(df)
print()
print(df.index)