
# coding: utf-8

# In[ ]:

import numpy as np
from PIL import Image 
import requests
from io import BytesIO
# setting
Q = np.array([[0.6,0.4,0.],[0.6,0.4,0.],[0.,0.4,0.6]])

# average rule 
def avg(Q):
    m = Q.shape[0]
    return np.sum(Q, axis=0)/m

# borda rule 
def borda(Q):
    return (avg(Q) == np.max(avg(Q)))/sum(avg(Q)== np.max(avg(Q)))

def maj(Q): 
    m = Q.shape[0]
    n = Q.shape[1]
    M = np.ones(n)
    for j in range(n):
        cl = np.delete(np.arange(n), j)
        wins = np.array([np.sum(Q[:,j]> Q[:,s])> m/2 for s in cl])
        if np.any(wins==False)==True:
            M[j]=0
    return M/np.sum(M)

def intersect(Q):
    m = Q.shape[0]
    n = Q.shape[1]
    prefs = (-Q).argsort()
    for j in range(n):
        options = np.ones(n)
        for i in range(m):
            threshold = (Q[i,:])[np.where(prefs[i,:]==j)]
            my_options = Q[i,:]>=threshold
            options *= my_options
        if np.any(options == 1):
            break
    return options/sum(options)

def happy_avg(Q):
    return np.sum(avg(Q) * np.prod(Q, axis=0))

def happy_borda(Q):
    return np.sum(borda(Q) *np.prod(Q, axis=0))
    
    

