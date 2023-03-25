import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# State file location/name
relative_location_name = '../data/news_data.json'

#Function: Reads in the json file
#Parameter: Pass in the file location/name
#Returns: The file that was read in
def read(relative_location_name):
    with open(relative_location_name, 'r') as f:
        out = json.load(f)
        return out

#Function: Calculates the number of entries items in a list
#Parameter: Give a list
#Return: A list of numbers [1,2,3,4,5,etc] as a function of items in the list    
def number_titles(titles):
    numb = []
    for i, x in enumerate(titles):
        numb.append(i+1)
    return numb

# Reading in the data with read function
data = read(relative_location_name)

#packing the data into convenient lists
titles = [value['title_valence'] for value in data]
title_valence = [valence['compound']for valence in titles]

comments = [value['comment_valence'] for value in data]
comment_valence = [valence['compound']for valence in comments]

#plotting
fig, ax = plt.subplots()

ax.hist(comment_valence, edgecolor="white", linewidth=1)

ax.set_xlim((-1,1))
