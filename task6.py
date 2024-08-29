import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# Load the dataset
df = pd.read_csv('C:\\Users\\Vasudev\\Downloads\\disney_movie_data_final.csv')

# Display the first and last 5 rows
print(df.head())
print(df.tail())

# Display column names
print(df.columns.values)

# Check for missing values
print(df.isna().sum())

# Information about the dataset
print(df.info())

# Remove rows with missing values
df = df.dropna()

# Histogram of numerical values
df.hist(bins=50, grid=False, figsize=(20, 15))
plt.show()

# q1: Distribution of IMDb Ratings 
plt.figure(figsize=(10, 6))
sns.histplot(df['imdb'], bins=20, kde=True, color='skyblue')
plt.title('IMDb Ratings for Disney Movies')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequency')
plt.show()

# q2: Box Office Revenue vs Budget 
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget (float)', y='Box office (float)', data=df, hue='Country', edgecolor='w')
plt.title('Revenue vs Budget for Disney Movies ')
plt.xlabel('Budget (in Millions)')
plt.ylabel('Box Office Revenue (in Millions)')
plt.show()

#3: Number of Movies Released Per Year
df['Release date (datetime)'] = pd.to_datetime(df['Release date (datetime)'], errors='coerce')
df['Release Year'] = df['Release date (datetime)'].dt.year
release_year_count_cleaned = df['Release Year'].value_counts().sort_index()

plt.figure(figsize=(14, 7))
sns.lineplot(x=release_year_count_cleaned.index, y=release_year_count_cleaned.values, marker='o')
plt.title('Number of Movies Released Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies Released')
plt.show()

#q4: Box Office Revenue by Production Company 
top_10_companies = df['Production company'].value_counts().nlargest(10).index
top_10_data = df[df['Production company'].isin(top_10_companies)]
box_office_by_company = top_10_data.groupby('Production company')['Box office (float)'].mean().sort_values()

plt.figure(figsize=(12, 8))
box_office_by_company.plot(kind='barh', color='lightcoral')
plt.title('Average Box Office Revenue by Production Company (Top 10)')
plt.xlabel('Average Box Office Revenue (in Millions)')
plt.ylabel('Production Company')
plt.show()
