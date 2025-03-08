import pandas as pd

df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)

mean_score = df.groupby('genre')['critic_score'].mean()
print(mean_score)

grp = df.groupby(['platform', 'genre'])
print(grp['critic_score'].mean())
print(grp)

# Split in groups
grp = df.groupby(['platform', 'genre'])
# Apply mean method and conbine in Series object
mean_score = grp['critic_score'].mean()
print(mean_score)
# Slit-Apply-Conbine in one step
print(df.groupby(['platform', 'genre'])['critic_score'].mean())

print('The agg() method')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)

agg_dict = {'critic_score': 'mean', 'jp_sales': 'sum'}

grp = df.groupby(['platform', 'genre'])
print(grp.agg(agg_dict))

# Using personal functions with agg()
print('The agg() method with personal functions')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)
def double_it(sales):
    sales = sales.sum() * 2 # multiplica la suma anterior por 2
    return sales

agg_dict = {'jp_sales': double_it}

grp = df.groupby(['platform', 'genre'])
print(grp.agg(agg_dict))

print('Ejercicio')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

grp = df.groupby('genre')

agg_dict = {'total_sales': 'sum', 'na_sales': 'mean', 'eu_sales': 'mean', 'jp_sales': 'mean'}

genre = grp.agg(agg_dict)

print(genre)