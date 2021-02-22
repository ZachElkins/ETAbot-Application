# ETAbot Application


## Problem:


Imagine you need to write a program for quickly finding location of things.
A user would enter information as "dance shoes - basement", "tent - garage", 
"passport - safe", "beer - fridge", "buckwheat - big pantry". Then the user 
would want to know where the beer is and use the program to tell. What data 
structure would you use to store the information and why? Please provide a 
sample python code of the core functionality and unit testing via github/gitlab 
or other way.


## Solution:


I decided to use the built in python dictionary structure. There is no need
for the items to be indexed in this sitaution, so a something like a list would
be unncessary and not scale well for larger applications.
