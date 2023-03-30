import nltk
import seaborn as sns
import praw
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sns.set(style='darkgrid', context='talk', palette='Dark2')
import json
from key_otto import client_id, client_secret, password, user_agent, username # change to key

# Get access
reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret, password = password,
                     user_agent = user_agent, username = username)

# Initialize parameters for search
sub_reddit = "worldnews"
number_of_posts = 1000
score_limit = 0


# This function gathers the submission titles and the post id's.
# Returns a list of titles and another list with the corresponding id's
# linked by index
# Parameters:
    # subreddit, number of posts, minimum score
def get_sub_title_id(sub, limitter, score_limit):
    submission_titles = []
    ID = []
    for submission in reddit.subreddit(sub).new(limit=limitter):
        if submission.score > score_limit:
            title = (submission.title)
            submission_titles.append(title)
            ID.append(submission.id)
            
    return submission_titles, ID


# Function: Gathers comments and votes. (No replies)
# Parameters: Pass in a list of post id's.
# Returns: comment forest list and votes for submission
def get_comment_score(ID):
    com = []
    votes = []
    for i in ID:
        submission = reddit.submission(id = i)
        votes.append(submission.score)
        out = submission.comments
        out.replace_more(limit=0)
        com.append(out)
    return com, votes

# Function: Simplifies the comment forest list and leaves out replies by BOT's
# Parameter: Pass in a comment forest list
# Returns: multiple lists of comments all in one list.
def simplify_comments(comments):
    comment_list_list = []
    for comment in comments:
        comment_list = []
        for i in comment._comments:
            text = i.body
            bot = "I am a bot" in text
            if i.author_flair_text != 'BOT' and bot == False:
                comment_list.append(text)
        comment_list_list.append(comment_list)
    return comment_list_list
            
# Function: Simple valence analysis on the text in all the titles and comments.
# Parameters: Pass in the list of submission titles and then comment_list_list (NOTE RIGHT ORDER)
# Returns: Valence analysis scores lists, titles_valence_list and comment_valence_list    
def sentiment(headlines, listing):
    sia = SIA()
    title_valence = []
    comment_valence = []
    for line in headlines:
        pol_score = sia.polarity_scores(line)
        pol_score['headline'] = line
        title_valence.append(pol_score)

    for comment_list in listing:
        textdump = str(comment_list)
        if len(textdump) != 2: # If there are no comments in the list the lenght will be 2 because of the square brackets.
             feel = sia.polarity_scores(textdump)
             comment_valence.append(feel)
        else: # If there was no comments on the post the post is marked for deletion (In the gather function)
            comment_valence.append("DELETE")
        
    return title_valence, comment_valence


#Function: Connects the variables into a list full of dictionaries (JSON friendly)
# Paramenters: headlines = list of titles, votes = score_list, titles_valence_list and comment_valence_list
# Returns: list full of dictionaries with all the information requested in parameters.
def gather(headlines, votes, title_valence, comment_valence):
    lizz = []
    for head,vote,t_val,c_val in zip(headlines, votes, title_valence, comment_valence):
        if c_val != "DELETE":
            data = {}
            data['headline'] = head
            data['votes'] = vote
            data['title_valence'] = t_val
            data['comment_valence'] = c_val
            lizz.append(data)
    return lizz

#Function: Saves a dictionary into a json file in the data folder.
#Parameters: Pass in the file you want to save 
def save(data):
    with open('../data/news_data_test.json', 'w') as f:
        json.dump(data, f, indent = 4)
        
                
# running sequence
headlines, ID = get_sub_title_id(sub_reddit, number_of_posts, score_limit)
comments, votes = get_comment_score(ID)        
listing = simplify_comments(comments)
title_valence, comment_valence = sentiment(headlines, listing)

data_press = gather(headlines, votes, title_valence, comment_valence)
save(data_press)

