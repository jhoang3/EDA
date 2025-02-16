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

# print(df.head())
# print(df.info()) # shows the data types of each column, all good
# print(df.describe()) # shows the statistics of the data

# check nulls
# print(df.isnull().sum()) # prints number of nulls