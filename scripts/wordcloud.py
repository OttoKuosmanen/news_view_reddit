from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np
import json

# File location relative
relative_location_name = '../data/news_data_file.json'

def read(relative_location_name):
    with open(relative_location_name, 'r') as f:
        out = json.load(f)
        return out


# Getting the titles and turning it into a string.

def distill(data):
    titles = []
    for i in data:
        titles.append(i['headline']) 
    cloud = str(titles)
    return cloud

# distilation of data
data = read(relative_location_name)
cloud = distill(data)

# Setting a mask image
mask = np.array(PIL.Image.open("map.jpg"))
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
