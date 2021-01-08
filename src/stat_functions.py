#!/usr/bin/env python
# coding: utf-8

# # Statistical Functions
# 
# This file contains functions to calculate the mean, dot product, standard deviation and corelation of the dataset.

# #### Import necessary packages:

# In[2]:


import pandas as pd
import numpy as np
import math 


# #### Calculate mean and return normalized mean

# In[3]:


def mean_normalize(var):

    mean = sum(var) / len(var)
    mean_norm = []
    
    for i in range(0,len(var)):
        mean_norm.append(var[i] - mean)
        
    return mean_norm


# #### Calculate dot product of the normalized means of two datasets

# In[4]:


def dot_product(x, y):
    
    dot_prod = 0
    
    for i in range(0,len(x)):
        dot_prod += (x[i] * y[i])
    return dot_prod


# #### Calculate standart deviation:

# In[5]:


def std_dv(mean_normalize):
    stddv = []
    
    
    for i in range(0,len(mean_normalize)):
        stddv.append(mean_normalize[i] ** 2)
    summ = sum (stddv)   
    return summ


# #### Calculate correlation between two datasets:

# In[6]:


def correlation(var1, var2):
    
    var1_mean = mean_normalize(var1)
    var2_mean = mean_normalize(var2)
    
    var_dpr = dot_product(var1_mean, var2_mean)
    
    var1_mean_sqr = std_dv(var1_mean)
    var2_mean_sqr = std_dv(var2_mean)
    
    correl = var_dpr / math.sqrt(var1_mean_sqr * var2_mean_sqr)
    
    return round(correl,2)


# In[ ]:




