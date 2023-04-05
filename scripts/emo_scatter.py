import numpy as np
import matplotlib.pyplot as plt
import json

# State file location/name
relative_location_name = '../data/news_data_file.json'

#Function: Reads in the json file
#Parameter: Pass in the file location/name
#Returns: The file that was read in
def read(relative_location_name):
    with open(relative_location_name, 'r') as f:
        out = json.load(f)
        return out

#Function: Sorts the valence scores into negative,neutral,postitive and the upvotes that are linked by index.
#Parameters: Pass in the list of valence scores of interest and the list of upvotes.
#Returns: list of valence scores and the linked list of upvotes, in the order of (positive, neutral, negative.)
def sort(valence, votes):
    negative = []
    positive = []
    neutral = []
    score_negative = []
    score_positive = []
    score_neutral = []
    for val, vote in zip(valence, votes):
        if val < 0:
            negative.append(val)
            score_negative.append(vote)
        elif val > 0:
            positive.append(val)
            score_positive.append(vote)
        elif val == 0:
            neutral.append(val)
            score_neutral.append(vote)
            
    return positive, score_positive, neutral, score_neutral, negative, score_negative,
    



# Reading in the data with read function
data = read(relative_location_name)

#packing the data into convenient lists
titles = [value['title_valence'] for value in data]
title_valence = [valence['compound']for valence in titles]

comments = [value['comment_valence'] for value in data]
comment_valence = [valence['compound']for valence in comments]

votes = [value['votes'] for value in data]

#Sorting based on valence.
positive, votes_positive, neutral, votes_neutral, negative, votes_negative = sort(comment_valence,votes)

# Converting valence to absolute valence.
negative = [abs(i) for i in negative]


#Plotting
plt.scatter(negative, votes_negative, color="blue", facecolor="cyan", label="Negative")
plt.scatter(neutral, votes_neutral, color='white', label='Neutral')
plt.scatter(positive, votes_positive, color='red', label='Positive',facecolor='orange')

# Add labels and title to the plot
plt.suptitle("Emotionality and Upvotes",fontsize=14, fontweight='bold')
plt.xlabel("Comment Emotionality", fontsize=14, fontweight='bold' )
plt.ylabel("Upvotes" ,fontsize=14, fontweight='bold')
plt.legend()


# Set the background color of the plot area to black
fig = plt.gca()
fig.set_facecolor('black')
plt.style.use('dark_background')



# Add a grid to the plot
plt.grid(alpha=0.1, color="cyan")

#figure size
plt.figure(figsize=(8, 6))

# Show the plot
plt.show()


