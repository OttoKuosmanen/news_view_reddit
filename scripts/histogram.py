# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:55:49 2023

@author: Otto
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.stats import spearmanr

# State file location/name
relative_location_name = '../data/news_data_file.json'

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
votes = [value['votes'] for value in data]

comments = [value['comment_valence'] for value in data]
comment_valence = [valence['compound']for valence in comments]

#getting usefull statistics from data
mean_comment = np.mean(comment_valence)
mean_title = np.mean(title_valence)
mean_votes = np.mean(votes)
median_comment = np.median(comment_valence)
median_title = np.median(title_valence)
median_vote = np.median(votes)
min_comment = np.min(comment_valence)
max_comment = np.max(comment_valence)
min_title = np.min(title_valence)
max_title = np.max(title_valence)
std_votes = np.std(votes)
min_votes = np.min(votes)

x = np.array(title_valence)
y = np.array(comment_valence)

print(mean_votes)
print(min_votes)

#plot style
plt.style.use('dark_background')

# create a figure object with 2 subplots
fig, axes = plt.subplots(nrows=2, ncols=1,figsize=(9, 6))

# add some space between subplots
fig.subplots_adjust(hspace=0.3)
axes[0].tick_params(axis='x', pad=10)
axes[1].tick_params(axis='x', pad=10)

# specifying the bin's
bins=[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

bins = np.linspace(-1, 1, num = 10)
#bins= np.arange(-1.05,1.05, 0.2)
#bins = [-0.1]

# plot data on each subplot
axes[0].hist(title_valence, bins=bins, color='cyan', edgecolor='black')
axes[1].hist(comment_valence,bins=bins, color='darkorange', edgecolor='black')

# add labels and title to each subplot
fig.text(0.05, 0.5, 'Frequency', ha='center', va='center', rotation='vertical', fontsize=15)
axes[0].set_title('News Titles', fontsize=16, fontweight='bold', color='cyan')
axes[1].set_xlabel('Valence of text' , fontsize=15)
axes[1].set_title('Comment Section', fontsize=16, fontweight='bold', color='darkorange')
axes[0].set_xlim((-1,1))
axes[1].set_xlim((-1,1))
axes[0].set_xticks((-1,-0.5,0,0.5,1))
axes[1].set_xticks((-1,-0.5,0,0.5,1))
axes[1].axvline(mean_comment, color='gold', label='Mean comment valence')
axes[0].axvline(mean_title, color='gold',label='Mean title valence')
axes[1].axvline(median_comment, color='gold', linestyle='dashed', label='Median comment valence')
axes[0].axvline(median_title, color='gold', linestyle='dashed', label='Median title valence')
axes[0].legend()
axes[1].legend()

# set grid styles
axes[1].grid(color='gold', alpha=0.2, linestyle='dashed')
axes[0].grid(color='cyan', alpha=0.2, linestyle='dashed')

# show the plot
plt.show()




