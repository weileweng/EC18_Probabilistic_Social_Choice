
# coding: utf-8

# In[ ]:

import numpy as np

# average rule 
def avg(Q):
    m = Q.shape[0]
    return np.sum(Q, axis=0)/m

# borda rule 
def borda(Q):
    def borda(Q):
    eps = 1e-10
    return (abs(avg(Q) - np.max(avg(Q)))<eps)/sum(avg(Q)== np.max(avg(Q)))
       
print("Borda rule: {}".format(borda(Q)))

# majority rule 
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

# Pareto rule
def pareto(Q):
    m = Q.shape[0]
    n = Q.shape[1]
    options = np.ones(n)
    for j in range(n):
        for s in np.delete(np.arange(n), j):
            if (np.all((Q[:,j]>= Q[:,s]))==True) & (np.any((Q[:,j]> Q[:,s]))==True):
                options[j]=0
    pareto = options/np.sum(options) if np.any(options==1)==False else np.ones(n)/n
    return pareto   

# Intersection rule
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

# average rule: probablity of every one obtained by desired outcome
def happy_avg(Q):
    return np.sum(avg(Q) * np.prod(Q, axis=0))

# borda rule: probablity of every one obtained by desired outcome
def happy_borda(Q):
    return np.sum(borda(Q) *np.prod(Q, axis=0))
    
    

