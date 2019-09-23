#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai/">
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png" width="200" align="center">
# </a>

# <h1>Sets in Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about the sets in the Python Programming Language. By the end of this lab, you'll know the basics set operations in Python, including what it is, operations and logic operations.</p> 

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <a href="https://cocl.us/topNotebooksPython101Coursera">
#          <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png" width="750" align="center">
#     </a>
# </div>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>
#             <a href="#set">Sets</a>
#             <ul>
#                 <li><a href="content">Set Content</a></li>
#                 <li><a href="op">Set Operations</a></li>
#                 <li><a href="logic">Sets Logic Operations</a></li>
#             </ul>
#         </li>
#         <li>
#             <a href="#quiz">Quiz on Sets</a>
#         </li>
#     </ul>
#     <p>
#         Estimated time needed: <strong>20 min</strong>
#     </p>
# </div>
# 
# <hr>

# <h2 id="set">Sets</h2>

# <h3 id="content">Set Content</h3>

# A set is a unique collection of objects in Python. You can denote a set with a curly bracket <b>{}</b>. Python will automatically remove duplicate items:

# In[1]:


# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# The process of mapping is illustrated in the figure:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsUnique.png" width="1100" />

#  You can also  create a set from a list as follows:

# In[2]:


# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19",               "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# Now let us create a set of  genres:

# In[3]:


# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",                     "progressive rock", "soft rock", "R&B", "disco"])
music_genres


# <h3 id="op">Set Operations</h3> 

# Let us go over set operations, as these can be used to change the set. Consider the set <b>A</b>:

# In[4]:


# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A


#  We can add an element to a set using the <code>add()</code> method: 

# In[5]:


# Add element to set

A.add("NSYNC")
A


#  If we add the same element twice, nothing will happen as there can be no duplicates in a set:
# 

# In[6]:


# Try to add duplicate element to the set

A.add("NSYNC")
A


#  We can remove an item from a set using the <code>remove</code> method:

# In[7]:


# Remove the element from set

A.remove("NSYNC")
A


#  We can verify if an element is in the set using the <code>in</code> command:

# In[8]:


# Verify if the element is in the set

"AC/DC" in A


# <h3 id="logic">Sets Logic Operations</h3>

# Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:

#  Consider the following two sets:

# In[9]:


# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsSamples.png" width="650" />

# In[10]:


# Print two sets

album_set1, album_set2


# As both sets contain <b>AC/DC</b> and <b>Back in Black</b> we represent these common elements with the intersection of two circles.

# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsLogic.png" width = "650" />

# You can find the intersect of two sets as follow using <code>&</code>:

# In[11]:


# Find the intersections

intersection = album_set1 & album_set2
intersection


# You can find all the elements that are only contained in <code>album_set1</code> using the <code>difference</code> method:

# In[12]:


# Find the difference in set1 but not set2

album_set1.difference(album_set2)  


# You only need to consider elements in <code>album_set1</code>; all the elements in <code>album_set2</code>, including the intersection, are not included.

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsLeft.png" width="650" />

# The elements in <code>album_set2</code> but not in <code>album_set1</code> is given by:

# In[13]:


album_set2.difference(album_set1)  


# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsRight.png" width="650" />

# You can also find the intersection of <code>album_list1</code> and <code>album_list2</code>, using the <code>intersection</code> method:

# In[14]:


# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   


#  This corresponds to the intersection of the two circles:

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsIntersect.png" width="650" />

# The union corresponds to all the elements in both sets, which is represented by coloring both circles:

# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%202/Images/SetsUnion.png" width="650" />

#  The union is given by:

# In[15]:


# Find the union of two sets

album_set1.union(album_set2)


# And you can check if a set is a superset or subset of another set, respectively, like this:

# In[16]:


# Check if superset

set(album_set1).issuperset(album_set2)   


# In[17]:


# Check if subset

set(album_set2).issubset(album_set1)     


# Here is an example where <code>issubset()</code> and <code>issuperset()</code> return true:

# In[18]:


# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 


# In[19]:


# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})   


# <hr>

# <h2 id="quiz">Quiz on Sets</h2>

# Convert the list <code>['rap','house','electronic music', 'rap']</code> to a set:

# In[20]:


# Write your code below and press Shift+Enter to execute

genres_set={'rap','house','electronic music','rap'}
genres_set


# Double-click __here__ for the solution.
# <!-- Your answer is below:
# set(['rap','house','electronic music','rap'])
# -->

# <hr>

# Consider the list <code>A = [1, 2, 2, 1]</code> and set <code>B = set([1, 2, 2, 1])</code>, does <code>sum(A) = sum(B)</code> 

# In[23]:


# Write your code below and press Shift+Enter to execute

A=[1, 2, 2, 1]
B=set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# A = [1, 2, 2, 1]  
# B = set([1, 2, 2, 1])
# print("the sum of A is:", sum(A))
# print("the sum of B is:", sum(B))
# -->

# <hr>

# Create a new set <code>album_set3</code> that is the union of <code>album_set1</code> and <code>album_set2</code>:

# In[24]:


# Write your code below and press Shift+Enter to execute

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set1
album_set2
album_set3


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_set3 = album_set1.union(album_set2)
# album_set3
# -->

# <hr>

# Find out if <code>album_set1</code> is a subset of <code>album_set3</code>:

# In[26]:


# Write your code below and press Shift+Enter to execute

set(album_set1).issubset(album_set3)


# Double-click __here__ for the solution.
# 
# <!-- Your answer is below:
# album_set1.issubset(album_set3)
# -->

# <hr>
# <h2>The last exercise!</h2>
# <p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href="https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/" target="_blank">this article</a> to learn how to share your work.
# <hr>

# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <h2>Get IBM Watson Studio free of charge!</h2>
#     <p><a href="https://cocl.us/bottemNotebooksPython101Coursera"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/BottomAd.png" width="750" align="center"></a></p>
# </div>

# <h3>About the Authors:</h3>  
# <p><a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a> is a Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>

# Other contributors: <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a>

# <hr>

# <p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>
