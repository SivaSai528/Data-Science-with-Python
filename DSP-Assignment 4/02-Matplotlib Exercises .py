#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Matplotlib Exercises 
# 
# Welcome to the exercises for reviewing matplotlib! Take your time with these, Matplotlib can be tricky to understand at first. These are relatively simple plots, but they can be hard if this is your first time with matplotlib, feel free to reference the solutions as you go along.
# 
# Also don't worry if you find the matplotlib syntax frustrating, we actually won't be using it that often throughout the course, we will switch to using seaborn and pandas built-in visualization capabilities. But, those are built-off of matplotlib, which is why it is still important to get exposure to it!
# 
# ** * NOTE: ALL THE COMMANDS FOR PLOTTING A FIGURE SHOULD ALL GO IN THE SAME CELL. SEPARATING THEM OUT INTO MULTIPLE CELLS MAY CAUSE NOTHING TO SHOW UP. * **
# 
# # Exercises
# 
# Follow the instructions to recreate the plots using this data:
# 
# ## Data

# In[1]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

# In[2]:


import matplotlib.pyplot as plt


# ## Exercise 1
# 
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

# In[15]:


Fig = plt.figure()
A = Fig.add_axes([0,0,1,1]) 
A.plot(x,y)
A.set_xlabel('x')
A.set_ylabel('y')
A.set_title('title')


# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

# In[5]:


Fig = plt.figure()
A1 = Fig.add_axes([0,0,1,1])
A2 = Fig.add_axes([0.2,0.5,.2,.2])


# ** Now plot (x,y) on both axes. And call your figure object to show it.**

# In[6]:


A1.plot(x,y)
A1.set_xlabel('x')
A1.set_ylabel('y')


A2.plot(x,y)
A2.set_xlabel('x')
A2.set_ylabel('y')
Fig


# ## Exercise 3
# 
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**

# In[7]:


Fig = plt.figure()

A = Fig.add_axes([0,0,1,1])
A2 = Fig.add_axes([0.2,0.5,.4,.4])


# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# In[8]:


A.plot(x,z)
A.set_xlabel('X-axis')
A.set_ylabel('Z-axis')


A2.plot(x,y)
A2.set_xlabel('X')
A2.set_ylabel('Y')
A2.set_title('zoom')
A2.set_xlim(20,22)
A2.set_ylim(30,50)

Fig


# ## Exercise 4
# 
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

# In[9]:


Fig, axes = plt.subplots(nrows=1, ncols=2)


# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**

# In[10]:


axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
Fig


# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.**

# In[11]:


Fig, Axes = plt.subplots(nrows=1, ncols=2,figsize=(12,2))

Axes[0].plot(x,y,color="blue", lw=5)
Axes[0].set_xlabel('x')
Axes[0].set_ylabel('y')

Axes[1].plot(x,z,color="red", lw=3, ls='--')
Axes[1].set_xlabel('x')
Axes[1].set_ylabel('z')


# # Great Job!
