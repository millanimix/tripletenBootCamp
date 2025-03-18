# Using matplotlib to create plots
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': [2, 3, 4, 5], 'b': [4, 9, 16, 25]})
print(df)

# df.plot()
# plt.show()

# Plotting one column
# df['b'].plot()
# plt.show()
# plt.savefig('myplot.png')

# Styles
# df.plot(title='A y B', style='o-')

# Axes
# df.plot(x='b', y='a', title='A vs B', style='o')

# Personal Labels
# df.plot(x='b',
#         y='a',
#         title='A vs B',
#         style='o',
#         xlabel='Hola, soy B',
#         ylabel='Hola,  soy A')

# Using methods to set axes labels
# df.plot(x='b',
#         y='a',
#         title='A vs B',
#         style='o',
#         legend=False)

# plt.xlabel('Hola, soy B')
# plt.ylabel('Hola, soy A')

# Axes Limits
# df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], ylim=0)

# Grid lines
# df.plot(x='b', y='a', title='A vs B', style='o', grid=True)

# Figure size
# Small plot
# df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], figsize=[2, 2])
# Large plot
# df.plot(x='b', y='a', title='A vs B', style='o', xlim=[0, 30], figsize=[10, 2])

# plt.show()

# Exercise
# df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})

# df.plot(x='c', y='a', title='A vs C', style='*', color='hotpink', figsize=[5, 5], xlim=[0, 12], ylim=[1, 6], xlabel='C', ylabel='A')
# plt.show()

# Scatter graph
df = pd.read_csv('04_Sprint4/datasets/height_weight.csv')
print(df.head())
print()
df.info()
print()
print(df.describe())

# df.plot(x='height', y='weight')
# df.sort_values('height').plot(x='height', y='weight')
# df.plot(x='height', y='weight', style='o')
# df.plot(x='height', y='weight', kind='scatter')
# df.plot(x='height', y='weight', kind='scatter', alpha=0.3)
# Exercise
# df.plot(x='age', y='height', kind='scatter', alpha=0.36, figsize=[8,6], xlabel='Age / years', ylabel='Height / inches', title='Adult heights' )
# plt.show()

print('Pearson\'s Correlation')
print(df['height'].corr(df['weight']))

print('Correlación height y age')
ah_corr = df['age'].corr(df['height'])
print(ah_corr)

print('\nCorrelación del dataframe')
print(df.corr())

print('Scatter matrix')
# pd.plotting.scatter_matrix(df, figsize=(9, 9))
# plt.show()

# Exercise
corr_mat = df.corr()
male_corr = corr_mat.loc['male', ['height', 'weight', 'age']]
print(male_corr)

# line graphs
df = pd.read_csv('04_Sprint4/datasets/sbux.csv')
print(df.head())
print()
df.info()

# df.plot(x='date', y='open')
# df.plot(x='date',
#         y='open',
#         legend=False,
#         title='Starbucks market open',
#         xlabel='Date',
#         ylabel='Share price / USD',
#         rot=45)
# plt.show()

# Exercise 1
# df.plot(x='date',
#         y='volume',
#         legend=False,
#         title='Historic SBUX volume',
#         xlabel='Date',
#         ylabel='Volume',
#         rot=50,
#         ylim=[1e6, 7e7])
# plt.show()

# Exercise 2
# cols = ['open', 'close']
# df.plot(x='date',
#         y=cols,
#         title='Historic SBUX price',
#         xlabel='Date',
#         ylabel='Share price / USD',
#         rot=50)
# plt.show()

# Bar graphs
df = pd.read_csv('04_Sprint4/datasets/west_coast_pop.csv')
df.info()
print(df)

# df.plot(x='year', kind='bar')
# df.plot(x='year',
#         kind='bar',
#         title='West coast USA population growth',
#         xlabel='Year',
#         ylabel='Population (millions)')

# plt.legend(['CA', 'OR', 'WA'])
# plt.show()

#Excersice
# cols = ['or_pop', 'wa_pop']
# df.plot(x='year',
#         y=['or_pop', 'wa_pop'],
#         kind='bar',
#         title='Pacific Northwest population growth',
#         xlabel='Year',
#         ylabel='Population (millions)')
# plt.legend(['OR', 'WA'])
# plt.show()


# Histograms
df = pd.read_csv('04_Sprint4/datasets/height_weight.csv')
# df.hist()
# df.plot(kind='hist')
# df.hist(column='height')
# df['height'].hist()
# df.hist(column='height', bins=30)
# df['height'].plot(kind='hist', bins=30)

# # esto mostrará el gráfico de hombres
# df[df['male'] == 1]['height'].plot(kind='hist', bins=30)
# # esto mostrará el gráfico de mujeres
# # e incluye un valor alpha para que podamos ver ambos histogramas por completo
# df[df['male'] == 0]['height'].plot(kind='hist', bins=30, alpha=0.8)
# plt.legend(['Male', 'Female']) # leyenda, que sigue el mismo orden trazado anteriormente

# df = df.sort_values('male').reset_index(drop=True)
# df = df[df.index < 5000]
# df.hist(column='height', bins=50)
# plt.show()

# Exercises 1
# separa df en dataframes separados según la edad
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

# print out the results
print("La suma de las longitudes del dataframe:", df_20s['age'].count() + df_30s['age'].count() + df_40s['age'].count())
print("Edad mínima y máxima para df_20s:", df_20s['age'].min(), df_20s['age'].max())
print("Edad mínima y máxima para df_30s:", df_30s['age'].min(), df_30s['age'].max())
print("Edad mínima y máxima para df_40s:", df_40s['age'].min(), df_40s['age'].max())

# Exercises 2
df_20s['weight'].plot(kind='hist', bins=20, title='Weight / lbs', ylabel='Frequency')
df_30s['weight'].plot(kind='hist', bins=20, alpha=0.6)
df_40s['weight'].plot(kind='hist', bins=20, alpha=0.3)
plt.legend(['20s', '30s', '40s'])
plt.show()