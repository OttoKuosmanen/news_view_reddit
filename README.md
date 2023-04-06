This directory includes a simple reddit data extraction with basic language analysis (VADER: VALENCE) and some basic templates for data visualization.
Additionally you will find a datafile that is ready for analysis in the DATA folder (worldnews: 1000 posts. 27.3.2023).

Author: Otto Kuosmanen
Data source: https://www.reddit.com 
	     subreddit: "worldnews" (Subreddit can be changed)
 
Contribute: send message to: https://github.com/Keijumies

#############################################################################################################################################################################
								##IMPORTANT##
	There is one important thing to note before starting. Some of the scripts require that you have your own access key. This can easily be done from the reddit website.
	For more information on this navigate to the KEY folder and open the script. (You will need a reddit account)

	Some of the scripts can be run with the default datafile. [wordclouds, histogram, emo_scatter]
	If you want to make your own datafiles and have access to live analysis follow the steps found in the KEY folder.
#############################################################################################################################################################################
	______SCRIPTS_______

	wordclouds.py : 	Visualize the titles of the posts in the data file with the WorldCloud library.
                	

	wordclouds_live.py : 	Get data form reddit and visualize the titles of the posts with the WorldCloud library.
                	
	
	create_data.py: 	Create your own data file. Get data from a subreddit of your choice. 
                		Perform a simple language analysis on both title and comments. 
                		(Valence scores: negative, postitive, compound) [Compound is used for later analysis as it is a cumulative valence score]
                		Saves an json file with, rating on posts, valence scores and the headline.
                		save location is the data folder, format is JSON.

	histogram: 		Performs a simple analysis on a data file. Outputs a histogram of the valence scores on titles and comments.
	
	emo_scatter: 		A script for making a scatterplot that shows the emotionality of the comment section and the rating of a post.


	reddit_average_time_live: 	A simple function that gives you the average time between posts in a subreddit of your choosing.

################################################################################################################################################## 