# Design Diary - Milestone 2

This Milestone represents a genuine milestone in my understanding of computer science. I had heard
of scripts but I never pursued learning the difference between a script and a program until now.
I have heard about scripting from friends and media, but I never took the time to look up scripts
since they were not an educational objective for me to meet in my classes. Without realizing what
tool was needed to implement my ideas, I have been thinking about automating different tasks for 
many years. E.g.- I have been into buying and selling cars on the private party market here in
Humboldt for years and I wanted a program to alert me to any cars that were listed below their 
"Blue Book" appraised value so I could purchase them without constantly monitoring the market myself.
This is just one example of many different tasks I have thought about automating, but had no idea 
how to implement or what to call such a program. This Milestone has given me a much more clear idea 
of what I would need to make such a script come to fruition. Although I have ideas for many different
scripts, I realize they are absolutely beyond my proficiency in Python to create at this point. I 
would like to make scripts to suit such needs, but for now I decided to stick with a simple script
to meet the objectives for this Milestone.

For my Milestone 2, I decided to stick with the default Milestone objective of accepting 2 or more
RSS feeds, filtering based on time, merging the feeds, and sorting those feeds based on time. I 
struggled with understanding the syntax of how the Python feedparser library worked. I struggled
figuring out how to get the date of the feeds for sorting after I modified the given code to filter 
based on the past 24 hours instead of past 1 hour. I ended up understanding how the code to filter 
could be written by writing a separate function and calling it or by using a lambda to achieve the 
same thing more succinctly and "pythonically". After that hurdle, my next hurdle was exporting the 
feed data as a .csv file. This took a bit of working through because I did not understand the 
difference between writing to a csv with a typical file write as opposed to writing to the a csv with 
a csvwriter function. The csv writer function ended up making my formatting easier to figure out since 
I wanted the column headings to display properly in Excel.  This was a rewarding Milestone and I am 
looking forward to continuing working with Python for creating the scripts to automate all of my other 
ideas.

![Milestone2Demo](https://github.com/rja45/scripting/Milestone02.gif)