import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Sentiment import title_valence, comment_valence, votes


#packing the data into convenient lists
compound_comments = [value['compound'] for value in comment_valence]
titles = [value['headline'] for value in title_valence]
compound_titles = [value['compound'] for value in title_valence]

#Building the lists into dictionary
data = {'title' : titles, 'title_valence': compound_titles, 'score': votes, 'comment_valence': compound_comments }
# Loading the dictionary into a dataframe
df = pd.DataFrame(data)

# Calculating the mean valence in all news titles: Scale -1(Negative) to 1(Positive)
title_mean = np.mean(compound_titles)

# Calculating the mean valence in all comment sections: Scale -1(Negative) to 1(Positive)
comment_mean = np.mean(compound_comments)


# Creating a function that counts the number of titles in the data
# Returns a list of numbers
def number_titles(titles):
    numb = []
    for i, x in enumerate(titles):
        numb.append(i+1)
    return numb

title_n = number_titles(titles)

"""fig, ax = plt.subplots()

ax.hist(compound_comments, edgecolor="white", linewidth=1)

#ax.set(ylim = (-1, 1))
ax.set_xlim((-1,1))
"""

fig, ax = plt.subplots()
plt.scatter(compound_titles, compound_comments, s=votes)
ax.set(ylim = (-1, 1))
ax.set_xlim((-1,1))
plt.show()

"""
///Quick news analysis///

Data I have: World Cloud of worldnews titles (1000:posts)
Average time between posts of worldnews (1000:posts)
Sentiment analysed data(Valence of text) from the text of world news titles.
    Each post and total-mean
Sentiment analysed data(Valence of text) from the text of world news comments to posts.
    Each thread and mean
How should i present it?, graph it?
density plot
scatter plot (Rating as bubble plot) 
"""

#WorldCloud
#bar chart with all "titles" and valence
#Connected bar chart that shows how the response to the article was in terms of valence
#Activity counter?