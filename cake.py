
# coding: utf-8

# In[ ]:

import numpy as np
from rules import avg
from PIL import Image 
import requests
from io import BytesIO
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# url={}
# url["strawberry"] = "https://driscolls.imgix.net/-/media/assets/recipes/fresh-strawberry-cake-recipe.ashx?                     w=2880&h=1588&fit=crop&crop=entropy&q=50&ixlib=imgixjs-3.1.0"
# url["vanilla"] = "https://livforcake.com/wp-content/uploads/2017/06/vanilla-cake-4.jpg"
# url["chocolate"] ="https://data.thefeedfeed.com/recommended/post_5164230.jpeg"

def show_cake(win_cake): 
    #response = requests.get(url[win_cake])
    #img = Image.open(BytesIO(response.content))
    img = Image.open('images/'+ win_cake + '.jpg')
    plt.figure(figsize = (8,8))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

