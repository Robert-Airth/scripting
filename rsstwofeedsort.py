import feedparser
import datetime
import time
from time import mktime
from dateutil import parser, tz
import os
import csv

def pub_date(x):
    return x.published_parsed

def parse_feeds(url1, url2):
    feed1 = feedparser.parse(url1) 
    feed2 = feedparser.parse(url2)
    a_day_ago = datetime.datetime.now() - datetime.timedelta(hours=24)
    recent_posts = [entry for entry in feed1.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > a_day_ago]
    recent_posts += [entry for entry in feed2.entries if datetime.datetime.fromtimestamp(mktime(entry.updated_parsed)) > a_day_ago]
    # the above lambdas filter by time updated to show only items from last hour

    recent_posts.sort(key=lambda x: x.updated)
    recent_posts.sort(key=pub_date)
    
    fields = ['Date/Time Published', 'Post Title', 'Link']

    with open('techfeed.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)       
        # writing the fields 
        csvwriter.writerow(fields)       
        # writing the data rows 
     
        for post in recent_posts:
            csvwriter.writerow([post.published, post.title, post.link])
            print("(", post.published, ") ", '\n', "   TITLE: ", post.title, '\n', "      LINK: ", post.link, " ", sep= "")
    
    
    
    print("done")
    
   

  

#def time_sort_posts(posts=posts, )




if __name__ == '__main__':
  parse_feeds('https://www.sciencedaily.com/rss/top/technology.xml',  'https://www.wired.com/feed/category/gear/latest/rss')



    
    