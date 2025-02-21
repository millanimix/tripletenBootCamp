# %% [markdown]
# # Data Preprocessing + Simple Pandas

# %% [markdown]
# The following will be an example of some good practices in data preprocessing using netflix show/movie data. 
# 
# Here is the URL to the data: https://www.kaggle.com/shivamb/netflix-shows

# %% [markdown]
# ## Imports

# %%
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# %%
df = pd.read_csv("webinars/S2_1_data_preprocessing/netflix_titles.csv")
df.head()

# %%
df.shape

# %% [markdown]
# ## Preprocessing

# %% [markdown]
# - Find and fill in any missing values 
# - Check for duplicates
# - Categorize data
# - Type the data appropriately
#  
#  
# Be ready to share your reasons for how you did these things!
# 
# 

# %%
df.info()

# %%
#Check for NAs
df.isna().sum()

# %%
df.isna().sum()/df.shape[0]

# %%
df["country"].value_counts().sort_values(ascending=False)

# %%
df["rating"].value_counts().sort_values(ascending=False)

# %%
df[["cast","director", "country", "rating"]] = df[["cast", "director", "country", "rating"]].fillna("Unknown")

# %%
# I could choose to get rid of rows to get rid of missing data
df = df.loc[df["date_added"].isna() == False, :] # df.dropna(axis=0, subset=['date_added'], inplace=True)


# %%
df.isna().sum()

df.loc[df["duration"].isna() == True, :]

df = df.loc[df["duration"].isna() == False, :]

# %%
df["date_added"] = pd.to_datetime(df["date_added"])
df["release_year"] = pd.to_datetime(df["release_year"], format="%Y")

# %%
#Check for duplicatess
duplicate = df[df.duplicated()]
duplicate

df["listed_in"][df["listed_in"].duplicated()]

# %%
df.head()

# %%
df.info()

# %%
#Create groups 
movies = df.loc[df["type"] == "Movie", :]
tv_shows = df.loc[df["type"] == "TV Show", :]

#Get groups on genre
dramas = df[df["listed_in"].str.contains("Drama")]

# %%
dramas

# %%
df.info()

# %% [markdown]
# ## Split Function

# %%
example = "Hi, my name is Daniel"

example_date = "01-01-2021"

example_phone_num = "(777)-555-999"

temp_list = example.split(", ")

temp_date_list =example_date.split("-")

area_code = example_phone_num.split("-")[0]

# %%
area_code

# %%
movies["duration"]

# %%
tv_shows["duration"]


type(movies["duration"].str.split(" ", expand = False))

# %%
movies["length"] = movies["duration"].str.split(" ", expand = True)[0].astype("int64")
tv_shows["seasons"] = tv_shows["duration"].str.split(" ", expand = True)[0].astype("int64")

movies
tv_shows

# %% [markdown]
# ## Some Data Exploration

# %% [markdown]
# ### Q: Does netflix have mostly newer or older movies?

# %%
movies.groupby("release_year")["show_id"].count().sort_values(ascending = False)
movies.groupby("release_year")["show_id"].count().sort_index(ascending = False)


# %%
def is_classic_modern_new(year):
    if year < pd.to_datetime(1990, format = "%Y"):
        return "classic"
    elif year >= pd.to_datetime(2019, format = "%Y"):
        return "new"
    else:
        return "modern"


# %%
movies["classic_modern_new"] = movies["release_year"].apply(is_classic_modern_new)

# %%
movies

# %%
movies.groupby("classic_modern_new")["show_id"].count().sort_values(ascending = False)

# %% [markdown]
# ### A: In this data, netflix has more newer movies!

# %% [markdown]
# #

# %% [markdown]
# ### Q: How many new movies on Netflix are rated G?

# %%
len(movies.loc[(movies["rating"] == "G") & (movies["classic_modern_new"] == "new"), :])

# %% [markdown]
# ### A: Two new movies are rated G

# %% [markdown]
# #

# %% [markdown]
# ### Q:Which were the dramas that were added to netflix before 2017?

# %%
dramas.loc[dramas["date_added"] < pd.to_datetime('2017-01-01'), ["type", "title", "date_added"]]

# %% [markdown]
# ### A: Resulting dataframe above!

# %%



