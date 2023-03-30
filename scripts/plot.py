import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# State file location/name
relative_location_name = '../data/news_data_test.json'

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

votes = [value['votes'] for value in data]

#getting usefull statistics from data
mean_comment = np.mean(comment_valence)
mean_title = np.mean(title_valence)
mean_score = np.mean(votes)
median_comment = np.median(comment_valence)
median_title = np.median(title_valence)
median_vote = np.median(votes)
min_comment = np.min(comment_valence)
max_comment = np.max(comment_valence)
min_title = np.min(title_valence)
max_title = np.max(title_valence)



#plotting
fig, axs = plt.subplots(2,figsize=(8, 8))

axs[0].set_xlabel("News Title Valence")
axs[1].set_xlabel("Comment Section Valence")

axs[0].set_ylabel("Frequency")
axs[1].set_ylabel("Frequency")

bins = np.linspace(-1, 1, num=20)

axs[0].hist(title_valence, edgecolor="white", linewidth=1, bins=bins)
axs[1].hist(comment_valence, edgecolor="white", linewidth=1, bins=bins)

fig.suptitle("Distribution of Valence")
axs[0].set_xlim((-1,1))
axs[1].set_xlim((-1,1))

plt.subplots_adjust(hspace=0.4)
plt.show()



