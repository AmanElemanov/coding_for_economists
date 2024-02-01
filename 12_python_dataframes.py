#Intro to pandas.DataFrames

import pandas as pd
import numpy as np

#Create some raw data to construct data frames (df)
data = {"Tokyo": 30_000_000,
        "New York": 20_000_000,
        "London": 50_000_000}

#Create df from dictionary
df = pd.DataFrame(data=data, index = [1])

print(df)



#Create a datafram from csv
df_raw = pd.read_csv("https://osf.io/yzntm/download")

#Inspect
print(df_raw.head())

#What are dimensions of our data
print(df_raw.shape)

#Access number of rows
print(df_raw.shape[0])

#Name of columns
print(df_raw.columns)

#Create new column: multiple ways of doing so
#df.nnights = 1
#df["nnights"] = 1
df = df_raw.assign(nnights = 1)

#Delete df_raw since we don't need it anymore
del df_raw

df = pd.read_csv("https://osf.io/yzntm/download")

#Let's check out accommodation variable
df["accommodationtype"].head()

#We want to clean this up
df.accommodationtype = df.accommodationtype.str.strip("@").str[1]

#How many nights in each accommodation type
df.accommodationtype.value_counts()

#To get rid off empty place
df.accommodationtype.replace("", "Unknown", inplace=True)
df.accommodationtype.value_counts()

#Look at the guestrating
df['guestreviewsrating'].head()

#Create clean variable for ratings
df['ratings'] = df['guestreviewsrating'].str.split('/').str[0]
df['ratings'].head()

#Convert to float
df['ratings'] = df['ratings'].astype(float)

#What is the average rating?
df['ratings'].mean()

#Exercise: there is a varible called center1distance. What is the average distance from the center?
df["center1distance"].head()
#Need to split at whitespace
df["distance"] = df["center1distance"].str.split(" ")
df["distance"].head()
df.distance = df.distance.str[0]
df.distance
df['distance'] = df['distance'].astype(float)

print(df.columns)
#There are few rating-related variables. let's check them
print(df.filter(regex="rating").head())

#Renaming variables
df.rename(columns = {"rating_reviewcount" : "rating_count", "rating_2ta" : "rating_ta"}, inplace=True)
print(df.filter(regex="rating").head())

#Rename the following variables:
#rating2_ta_reviewcount : ratingta_count
#addresscountryname : country
#starrating : stars
#s_city : city
df.rename(columns = {"rating2_ta_reviewcount" : "ratingt_count", "addresscountryname" : "country", "starrating" : "stars", "s_city" : "city"}, inplace=True)
print(df.columns)

#Subsetting data
#Only look at hotels
df.loc[df.accommodationtype == "Hotel"]

#How to check for missing values?
print(df.ratings.isnull().sum())

#How many missing per country?
print(df.ratings.isnull().groupby(df.country)sum())
