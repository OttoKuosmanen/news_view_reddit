This directory includes easy reddit data extraction and some basic language analysis templates.

Author: Otto Kuosmanen
Data source: https://www.reddit.com/, subreddit "world news" by default but can be easily changed 
Contribute: send message to: https://github.com/Keijumies

	______SCRIPTS_______

	Wordclouds.py : Get data form reddit and visualize the titles of the posts with the WorldCloud library.
                	You can specify if you want it straight from the live data or from your own json file
	
	Sentiment.py :  Create your own data set.  
                	Perform a simple language analysis on both title and comments. 
                	(Valence scores: negative, postitive, compound) [Compound is used for later analysis as it is a cumulative valence score]
                	Saves an json file with, rating on posts, valence scores and the headline.
                	save location is the data folder, format is JSON

	
	
	
	todooos
	# Add access information to the document / need to create a new access info.