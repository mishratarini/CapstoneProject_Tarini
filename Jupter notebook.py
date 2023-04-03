#!/usr/bin/env python
# coding: utf-8

# Capstone Project

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
data_frame = pd.read_csv('ifood_df.csv')
data_frame.head()


# In[2]:


# Removing Duplicates
data_frame.drop_duplicates(inplace = True)


# In[3]:


# Checking Null duplicates
data_frame.isnull().any()


# In[4]:


# Remove Null values incase awe have any
thresh = len(data_frame)*0.6
data_frame.dropna(thresh=thresh, axis = 0).shape


# In[5]:


# convert Income from Float to Int
data_frame.Income.value_counts()
data_frame['Income'] = data_frame['Income'].apply(int)
data_frame.Income.value_counts()


# In[6]:


#Visualizations
data_frame.hist('Income')


# In[7]:


numeric = data_frame._get_numeric_data()


# In[8]:


# Removing Extreme Outliers
data_frame_outliers = data_frame[(data_frame.Income < data_frame.Income.quantile(0.995)) & (data_frame.Income > data_frame.Income.quantile(0.005))]
data_frame_outliers.hist('Income')


# In[9]:


# Sum of food purchased
data_frame['MntTotal'] = data_frame.loc[:,['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts']].sum(axis=1)
data_frame.MntTotal.head()


# In[10]:


data_frame.hist( column = ['Age', 'Customer_Days', 'Income', 'Kidhome', 'Teenhome'], figsize=(25,15))


# In[11]:


data_frame.hist( column = ['education_Basic', 'education_Graduation', 'education_Master', 'education_PhD'], figsize=(25,15))


# In[12]:


data_frame.hist( column = ['marital_Divorced', 'marital_Married', 'marital_Single', 'marital_Together', 'marital_Widow'], figsize=(25,15))


# In[ ]:





# In[ ]:




