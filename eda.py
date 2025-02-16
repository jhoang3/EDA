# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path to the file you'd like to load
path = kagglehub.dataset_download("yeganehbavafa/vnl-men-2023")

# Load version 2 of the dataset
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "yeganehbavafa/vnl-men-2023/versions/2",
  "VNL2023.csv",  
)

# 1. Data Understanding

# print(df.head())
# print(df.info()) # shows the data types of each column, all good
# print(df.describe()) # shows the statistics of the data

# check nulls
# print(df.isnull().sum()) # prints number of nulls

# check duplicates
# print(df.duplicated().sum()) # returned 0 duplicates

# print(df.query('Age < 21').count()) # 0 rows with age < 21


# sns.pairplot(noStrs, vars = ['Age', 'Attack', 
#                             #  'Block', 'Serve', 'Set', 
#                              'Dig', 'Receive'])

# sns.scatterplot(noStrs, x = "Block", y = "Attack")
# sns.displot(df, x="Country") # displot is for categorical data, shows the counts of each country

# plt.show()

# 2. Data Preparation
# can use py -i eda.py to run interactively
# can run df.columns to get all column names to use if needed, its needed
noStrs = df[[
                # 'Player', 
                # 'Country', 
                'Age', 'Attack', 'Block', 'Serve', 'Set', 'Dig',
                'Receive', 
                # 'Position'
                ]].copy() # copy dataset with only numerical values
# can also say df.drop(['...'], axis = 1) to drop columns

# can also do df.rename(columns= {'ogName': 'newName'}) to rename columns

# remove duplicates ex: df.loc[~df.duplicated(subset=['col1', 'col2'])].reset_index
    # ~ is the not operator, so it will return all rows that are not duplicates based on the subset

