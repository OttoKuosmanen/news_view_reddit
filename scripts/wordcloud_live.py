import praw
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np
import sys
sys.path.append('../KEY')
from key import client_id, client_secret, password, user_agent, username

# gain access to reddit
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret, password = password,
                     user_agent = user_agent, username = username)

# Initialize parameters for search
sub_reddit = "volvo"
number_of_posts = 100
score_limit = 0

# Function for requesting the titles from a subreddit. Returns them as a list.
# Parameters: 
#   sub = "subreddit", limitter = how many posts to is considered in the search, score_limit = minimum score for post to be included.
# Return: list of submission titles
def get_sub(sub, limitter, score_limit):
    submission_titles = []
    for submission in reddit.subreddit(sub).new(limit=limitter):
        if submission.score > score_limit:
            title = (submission.title)
            submission_titles.append(title)
            
    return submission_titles

# Getting the titles and turning it into a string.
titles = get_sub(sub_reddit,number_of_posts,score_limit)
cloud = str(titles)

# Setting a mask image
mask = np.array(PIL.Image.open("../IMG/map.jpg"))
mask[mask == 0] = 10 

stopwords = set(STOPWORDS)
stopwords.update(["s","U"])

# Generate a word cloud image
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10, stopwords = stopwords, mask=mask).generate(cloud)

# Display the generated image:
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

# Show the plot
plt.show()