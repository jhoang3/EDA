# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

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

# 3. Feature Understanding
# can use df.corr() to get the correlation between columns, numerical heatmap basically
# print(noStrs.corr())
# print(df['Age'].value_counts()) # gets us the counts of each age 

# ax = df['Age'].value_counts().plot(kind='bar', title='Age Distribution', ) 
# ax.set_ylabel('Count')
# plots counts of each age in a bar graph, barh for horiz
# plt.show()

# ax = df['Attack'].plot(kind='hist', title='Attack Distribution', bins=10)
# doing kind=kde gives a kernel density

# ax.set_xlabel('Average Attack')
# plt.show()

# 4. Feature Relationships
# print(noStrs.columns) # just to remind what columns we have

# lets anaylze the relationship between attack and block
# ax = sns.scatterplot(data=noStrs, x = "Block", y = "Attack",
#                 hue='Age')
# ax.set_title('Attack vs Block')
# plt.show()
# there seems to be a positive correlation between attack and block

# lets see the relationship between multiple features
# ax = sns.pairplot(data=noStrs, vars= [
#                                     # 'Age', 
#                                     'Attack', 'Block', 
#                                     #  'Serve', 
#                                     'Set', 'Dig', 'Receive']
#                                     , hue = 'Age', kind='scatter')
# plt.show()

# lets see the correlation values plotte
# sns.heatmap(noStrs.corr(), annot=True)
# plt.show()

# 5. Ask a question

# my question: What are the top 5 countries in each category (Attack, Block, Set, Dig, Receive)?

# df.groupby('Country')['Attack'].agg(['mean'])\
#     .sort_values(by='mean', ascending=False)\
#     .head(5).plot(kind='bar', title='Top 5 Countries by Attack')
# plt.show()

# df.groupby('Country')['Block'].agg(['mean'])\
#     .sort_values(by='mean', ascending=False)\
#     .head(5).plot(kind='bar', title='Top 5 Countries by Block')
# plt.show()
# df.groupby('Country')['Set'].agg(['mean'])\
#     .sort_values(by='mean', ascending=False)\
#     .head(5).plot(kind='bar', title='Top 5 Countries by Set')
# plt.show()
# df.groupby('Country')['Dig'].agg(['mean'])\
#     .sort_values(by='mean', ascending=False)\
#     .head(5).plot(kind='bar', title='Top 5 Countries by Dig')
# plt.show()
# df.groupby('Country')['Receive'].agg(['mean'])\
#     .sort_values(by='mean', ascending=False)\
#     .head(5).plot(kind='bar', title='Top 5 Countries by Receive')
# plt.show()

# group the data by country -> look at the attack col -> get the mean and 
# sort by descending mean

# try to find the top 5 overall by averaging attack, block, set, dig, receive 
df['Overall'] = df[['Attack', 'Block', 'Set', 'Dig', 'Receive']].mean(axis=1)
# ^ this creates a new column called overall that is the average of the 5 specified columns
print(df.groupby('Country')['Overall'].agg(['mean'])
    .sort_values(by='mean', ascending=False)
    .head(5))
    # .plot(kind='bar', title='Top 5 Countries Overall'))
# .agg is used to specify the aggregation function, in this case mean, can be sum, count, etc

# what is the top player for each country given their overall score
print(df.loc[df.groupby('Country')['Overall'].idxmax()][['Country', 'Player', 'Overall']].sort_values(by='Overall', ascending=False))

# what this does: .loc selects [row][col] to view
    # df.groupby('Country') groups all countries together
        # ['Overall'] views the overall score column
            # .idmax() gets the index of the max value for each country
                # so .loc will get the row of the max value for each country
    # [['Country', 'Player', 'Overall']] selects the columns we want to display