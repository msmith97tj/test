#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install ipywidgets


# In[2]:
# try 3 this one i added a comment so  I can test diff in github


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact, interact_manual


# In[3]:


iris = pd.read_csv('IRIS.csv')


# In[4]:


iris.head()


# In[5]:


@interact
def show_articles_more_than(column = 'sepal_length', x=5):
    return iris.loc[iris[column] > x]


# In[6]:


iris.shape


# In[7]:


iris.describe


# In[8]:


iris.duplicated().head()


# In[9]:


iris.duplicated().sum()


# In[10]:


iris.drop_duplicates(keep=False, inplace=True)


# In[11]:


iris.duplicated().sum()


# In[14]:


plt.figure(figsize = (8, 6))
plt.hist(iris['sepal_length'],
    bins = 20, color = "g")
plt.xlabel("Sepal Length")
plt.ylabel("Count")


# In[17]:


fig, ax = plt.subplots(1, 2, 
                       figsize = (15, 6))

iris.plot(x = 'sepal_length', y = 'sepal_width',
    kind = 'scatter', ax = ax[0],
    sharex = False, sharey = False,
    label = 'sepal', color = 'r')
    
iris.plot(x = 'petal_length', y = 'petal_width',
    kind = 'scatter', ax = ax[1],
    sharex = False, sharey = False,
    label = 'petal', color = 'b')


# use Iris-setosa Iris-virginica  in the filter

# In[20]:


def plot(species):
    data = iris[iris.species == species]
    
    data.plot.scatter('sepal_length',
                     'sepal_width')
    
interact(plot, kind = 'scatter',
    species = 'Iris-virginica')


# In[ ]:





# In[ ]:




