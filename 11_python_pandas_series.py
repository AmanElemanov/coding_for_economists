#Introduction to pandas and numpy
#Pandas in a python library for data manipulation

import pandas as pd
import numpy as np

#Let's look at pd.Series
#A series is a one-dimensional array of data

#Let's define our first pd.Series
#Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
ps = pd.Series(['a', 1, 2, np.pi])
print(ps)

#Which data type does our pd.Series have?
print(type(ps))

#We can access the values
print(ps, ps.values)

#We can access elements of pd.Series by indexing
print(ps[0:2])

#Define a custom index
series_1 = pd.Series(
  data = ["Schitzel",
         "Lemonade",
         "Whiskey"],
  index = ["Food",
          "Soda",
          "Alcohol"]
)

#Advance indexing of pd.Series
#using .loc[]
series_1.loc["Food"]
#Acessing more than a single index
series_1.loc[["Food", "Alcohol"]]

#using .iloc[] - using indexes rather than lables
series_1.iloc[0]

#Access elements from a range of indexes
print(series_1.loc["Food":"Alcohol"])
