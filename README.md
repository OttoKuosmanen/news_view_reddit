# Reddit Data Extraction and Basic Language Analysis

This directory provides tools for extracting data from Reddit, performing basic language analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner), and visualizing the data. The package includes a ready-to-analyze data file from the "worldnews" subreddit as of March 27, 2023.

**Author:** Otto Kuosmanen  
**Data Source:** [Reddit](https://www.reddit.com)  
**Subreddit:** "worldnews" (modifiable)  
**Contribute:** [GitHub](https://github.com/Keijumies)

---

### **Important Note**

Before starting, it is essential to understand that some scripts require your own Reddit access key. This can be obtained through the Reddit website. For more information, refer to the KEY folder's script. A Reddit account is necessary for this step.

Certain scripts can be executed with the default data file, including word clouds, histograms, and emotion scatter plots. To conduct live analysis or create your own data files, follow the instructions found in the KEY folder.

---

## Scripts

### Visualization

- **wordclouds.py**: Visualizes the post titles in the data file using the WordCloud library.

- **wordclouds_live.py**: Fetches data from Reddit and visualizes post titles with the WordCloud library.

### Data Creation

- **create_data.py**: Generates a custom data file by fetching data from a chosen subreddit. Performs basic language analysis on titles and comments, calculating valence scores (negative, positive, compound). The compound score is utilized for further analysis as it aggregates valence scores. The data is saved in JSON format in the data folder.

### Analysis

- **histogram**: Analyzes a data file and produces a histogram of the valence scores for titles and comments.

- **emo_scatter**: Creates a scatter plot illustrating the emotionality of comments and the post rating.

- **reddit_average_time_live**: Calculates the average time between posts in a selected subreddit.

---

### Data File

Located in the DATA folder, the file contains 1000 posts from the "worldnews" subreddit, dated March 27, 2023, ready for analysis.
