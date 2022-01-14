from re import sub
import praw 
import json
import requests

credentials = 'client_secrets.json'

with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

sub = "wallstreetbets"              # Choose your subreddit
titles = []
limit = 0
posts = 0
post_flairs = {'Daily Discussion', 'Weekend Discussion', 'Discussion'} 
a_comments = []


subreddit = reddit.subreddit(sub)  # Initialize the subreddit to a variable

# Sort by hot
hot_wsb = subreddit.hot()

for submission in hot_wsb:
    flair = submission.link_flair_text

    # Sort by flairs
    if flair in post_flairs:
        posts = +1
        submission.comments.replace_more(limit=limit)  
        comments = submission.comments 
        for top_comments in comments:
            a_comments.append(top_comments.body)

print(posts, a_comments)
### Extracting Comments from daily discussion 
# 
# TODO: 
#  - Extract comments from earnings 
#  - 

