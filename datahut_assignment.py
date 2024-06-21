#!/usr/bin/env python
# coding: utf-8

# QA/QC INTERNSHIP ASSIGNMENT

# JUNE 2024

# AUTHOR: ASWANY SADANAND

# #importing necessary libraries

# In[116]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #loading dataset

# In[117]:


df=pd.read_csv('Downloads/messy_data.csv')


# In[118]:


df


# In[119]:


df.info


# #checking null values

# In[120]:


df.isnull().sum()


# #checking name column

# In[121]:


# Cleaning the name column
df['Name'] = df['Name'].astype(str)               # Ensure all entries are strings
df['Name'] = df['Name'].str.strip()               # Trim leading and trailing whitespace
df['Name'] = df['Name'].str.title()               # Convert to title case
df['Name'] = df['Name'].str.replace(r'[^a-zA-Z\s]', '', regex=True)  # Remove special characters

# Handling missing values
df['Name'] = df['Name'].replace('Nan', 'Unknown') # Replace 'NaN' string with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')         # Fill actual NaN values with 'Unknown'

# Remove duplicates
df = df.drop_duplicates(subset=['Name'])


# In[122]:


df


# #checking age column

# In[123]:


df['Age'].value_counts()


# In[124]:


# Displaying the first few rows of the age column
print(df['Age'].head())

# Getting basic statistics of the age column
print(df['Age'].describe())

# Checking for missing values in the age column
print(df['Age'].isnull().sum())

# Filling missing values with the mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Detecting and handling outliers using IQR method
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Defining outlier range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Removing outliers
df= df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]

# Defining valid age range
min_age = 0
max_age = 120

# Removing invalid age values
df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

# Displaying the cleaned age column
print(df['Age'].describe())


# In[125]:


df


# In[126]:


df['Age'].value_counts()


# In[127]:


# Remove values after the decimal points in the Age column
df['Age'] = df['Age'].astype(int)


# In[128]:


df


# #checking email column

# In[129]:


df['Email'].value_counts()


# #checking for valid email addresses and replace invalid email address as 'unknown'

# In[130]:


# Defining a regex pattern for valid email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Replacing invalid email addresses as 'unknown'
df['Email'] = df['Email'].apply(lambda x: x if pd.notna(x) and pd.Series(x).str.match(email_pattern).any() else 'unknown')


# In[131]:


df['Email'].isnull().sum()


# In[132]:


df


# #checking Join date column

# In[133]:


df['Join Date'].value_counts()


# In[134]:


def parse_date(date_str):
    try:
        # Try parsing with a known format (ISO 8601, e.g., '2021-01-01')
        return pd.to_datetime(date_str, format='%Y-%m-%d', errors='raise')
    except ValueError:
        try:
            # If failed, try parsing with dayfirst=True for formats like '15/02/2021'
            return pd.to_datetime(date_str, dayfirst=True, errors='raise')
        except ValueError:
            try:
                # If both attempts fail, use dateutil parser for more complex formats
                return parser.parse(date_str)
            except (parser.ParserError, TypeError):
                # If all parsing attempts fail, return NaT
                return pd.NaT

# Apply the custom function to 'Join Date'
df['Join Date'] = df['Join Date'].apply(parse_date)

# Create a new column with the date in 'YYYY-MM-DD' format
df['date_year_first'] = df['Join Date'].dt.strftime('%Y-%m-%d')


# In[135]:


df


# #drop join date column

# In[140]:


cols_to_drop=['Join Date']


# In[141]:


df.drop(cols_to_drop,axis=1,inplace=True)


# #rename date_year_first column as Join Date

# In[142]:


df = df.rename(columns={'date_year_first': 'Join Date'})


# In[143]:


#fill NaN values in join date column as Unknown


# In[144]:


df['Join Date']=df['Join Date'].fillna('unknown')


# In[145]:


df


# #checking salary column

# In[146]:


df['Salary'].value_counts()


# In[147]:


df['Salary'].dtype


# In[148]:


missing_values_count = df['Salary'].isnull().sum()


# In[149]:


print("Number of missing values in the 'Salary' column:", missing_values_count)


# In[150]:


# Replace NaN values with the mean salary
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)


# In[151]:


df


# #remove value after the decimal points in the salary column

# In[152]:


# Remove values after the decimal points in the Salary column
df['Salary'] = df['Salary'].astype(int)


# In[153]:


df


# In[154]:


df['Salary'].dtype


# #checking department column

# In[155]:


df['Department'].value_counts()


# #mapping and removing invalid department names

# In[156]:


# Mapping dictionary
department_mapping = {
    'support': 'Support',
    'hr': 'HR',
    'marketing': 'Marketing',
    'sales': 'Sales',
    'engineering':"Engineering"
}

# Correcting the department names using replace
df['Department'] = df['Department'].replace(department_mapping)

# Identifying valid departments
valid_departments = set(department_mapping.values())

# Filtering out invalid departments
df = df[df['Department'].isin(valid_departments)]


# In[157]:


df['Department'].value_counts()


# In[158]:


df


# #dropping duplicate rows

# In[159]:


df.drop_duplicates()


# #save the cleaned dataframe as cleaned_data.csv

# In[160]:


df.to_csv('cleaned_data.csv', index=False)


# In[161]:


df


# In[162]:


df2=pd.read_csv('cleaned_data.csv')


# In[163]:


df2


# In[164]:


print("DataFrame saved to cleaned_data.csv")


# In[165]:


from IPython.display import FileLink


# In[166]:


# Create a download link
FileLink('cleaned_data.csv')


# In[ ]:




