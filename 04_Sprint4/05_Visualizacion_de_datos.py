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
df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})

df.plot(x='c', y='a', title='A vs C', style='*', color='hotpink', figsize=[5, 5], xlim=[0, 12], ylim=[1, 6], xlabel='C', ylabel='A')
plt.show()