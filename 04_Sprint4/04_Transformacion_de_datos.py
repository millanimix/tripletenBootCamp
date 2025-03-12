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

print('Pivot Tables')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
print(df.head())

df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)

pivot_data = df.pivot_table(index='genre',
                            columns= 'platform',
                            values='eu_sales',
                            aggfunc='sum')

print(pivot_data)
print()
print(type(pivot_data))

# Groupby example
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df.dropna(inplace=True)

groupby_data = df.groupby(['genre', 'platform'])['eu_sales'].mean()
print(groupby_data)
print()
print(type(groupby_data))

print('Ejercicio')
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df_pivot = df.pivot_table(index='genre', columns='year_of_release', values='jp_sales', aggfunc='mean')
print(df_pivot)

# DataFrames combine with concat()
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
print(df.head())

# Groupby example
mean_score = df.groupby('publisher')['critic_score'].mean()
print(mean_score)

df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']
num_sales = df.groupby('publisher')['total_sales'].sum()
print(num_sales)

# Concatenating two DataFrames
df_concat = pd.concat([mean_score, num_sales], axis='columns')
print(df_concat)

# Change column names
df_concat.columns = ['avg_critic_score', 'total_sales']
print(df_concat)

# Concataning rows
rpgs = df[df['genre'] == 'Role-Playing']
platformers = df[df['genre'] == 'Platform']

# Same columns but different rows. 
print(rpgs.head())
print(platformers.head())

df_concat = pd.concat([rpgs, platformers])
print(df_concat[['name', 'genre']])

# Exiercise
df = pd.read_csv('04_Sprint4/datasets/vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()
print(total_sales)

print('num_pubs')
num_pubs = df.groupby('platform')['publisher'].nunique()
print(num_pubs)

platforms = pd.concat([total_sales, num_pubs], axis=1)
platforms.columns = ['total_sales', 'num_publishers']
print(platforms)

# Combining DataFrames with merge()
first_pupil_df = pd.DataFrame(
    {
        'author': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
        'title': ['Little Women',
                  'The Great Gatsby',
                  'Of Mice and Men',
                  'The Adventures of Tom Sawyer',
                  'The Old Man and the Sea'
                 ],
    }
)
second_pupil_df = pd.DataFrame(
    {
        'author': ['Steinbeck', 'Twain', 'Hemingway', 'Salinger', 'Hawthorne'],
        'title': ['East of Eden',
                  'The Adventures of Huckleberry Finn',
                  'For Whom the Bell Tolls',
                  'The Catcher in the Rye',
                  'The Scarlett Letter'
                 ],
    }
)

print(first_pupil_df)
print()
print(second_pupil_df)

print('Inner merge')
# Inner merge
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='inner')
print(both_pupils)

print('Outer merge')
# Outer merge
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='outer')
print(both_pupils)

print('Left merge')
# Left merge
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='left')
print(both_pupils)

print('Right merge')
# Right merge
both_pupils = first_pupil_df.merge(second_pupil_df, on='author', how='right')
print(both_pupils)

print('Setting Personal sufix')
both_pupils = first_pupil_df.merge(second_pupil_df,
                                   on='author',
                                   suffixes=['_1st_student', '_2nd_student']
                                   )
print(both_pupils)

print()
# The merge column have diffrent names in both dataframes, so we need to rename it
first_pupil_df = pd.DataFrame(
    {
        'authors': ['Alcott', 'Fitzgerald', 'Steinbeck', 'Twain', 'Hemingway'],
        'title': ['Little Women',
                  'The Great Gatsby',
                  'Of Mice and Men',
                  'The Adventures of Tom Sawyer',
                  'The Old Man and the Sea'
                 ],
    }
)
second_pupil_df = pd.DataFrame(
    {
        'author': ['Steinbeck', 'Twain', 'Hemingway', 'Salinger', 'Hawthorne'],
        'title': ['East of Eden',
                  'The Adventures of Huckleberry Finn',
                  'For Whom the Bell Tolls',
                  'The Catcher in the Rye',
                  'The Scarlett Letter'
                 ],
    }
)

both_pupils = first_pupil_df.merge(second_pupil_df,
                                   left_on='authors',
                                   right_on='author'
                                   )
print(both_pupils)

# The drop() method
print('\nThe drop method')
print(both_pupils.drop('author', axis='columns'))

# Exercise
df_members = pd.read_csv('04_Sprint4/datasets/new_members.csv')