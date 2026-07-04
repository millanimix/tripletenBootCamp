import pandas as pd

# Obtener el valor máximo de una columna
df = pd.read_csv('06_Sprint6/datasets/music_log_processed.csv')
print(df['total_play'].max())

# Obtener la fila de un DataFrame con el valor máximo de una columna
print(df[df['total_play'] == df['total_play'].max()])

# Ejercicio: Buscar la reproducción más larga de una pista pop
pop_tracks = df[df['genre'] == 'pop']
pop_tracks = pop_tracks[pop_tracks['total_play'] > 30]
# max_dur = pop_tracks[pop_tracks['total_play'] == pop_tracks['total_play'].max()]
max_dur = pop_tracks['total_play'].max()
print(max_dur)

# Minimo
df_drop_skip = df[df['total_play'] > 30]
# Obtener el valor mínimo de una columna
print(df_drop_skip['total_play'].min())
# Obtener la fila de un DataFrame con el valor mínimo de una columna
print(df_drop_skip[df_drop_skip['total_play'] == df_drop_skip['total_play'].min()])

# Mediana
print(df['total_play'].median())
print(df_drop_skip['total_play'].median())

# Media
print(df_drop_skip['total_play'].mean())

# Ejercicio: Calcular los valores medios y medianos para la columna 'total_play'
pop_mean = pop_tracks['total_play'].mean()
pop_median = pop_tracks['total_play'].median()

print(pop_mean)
print(pop_median)