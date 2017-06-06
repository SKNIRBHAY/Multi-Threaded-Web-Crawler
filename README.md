# Multi-Threaded-Web-Crawler

 Definition: 
- A web crawler is a program which takes in a web URL and returns all the URLs on that website.

 Description:
- Developed Python program which takes in the homepage URL and returns all the links on that website.
- Made the program 8 times faster by using multi-threaded approach in Python.
- Used Queue library in Python to manage all the tasks between the threads to avoid race around condition.

 Working: 
- This web crawler expects two input from a user (i.e. a project name and the URL of the home page of the website to be crawled) and then it updates a text file name "crawled.txt" with all the links on the whole website. The user can feed the required input in the "main.py" file. 
