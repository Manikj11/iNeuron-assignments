#!/usr/bin/env python
# coding: utf-8

# ### 1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[5]:


i=2000
while (i<=3200):
    if i%7==0 and i%5!=0:
        print(i,end=",")
    i+=1


# In[3]:


for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=",")
    
    


# ### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[13]:


f_name,l_name= (input("Enter your name= ")).split()
rev_f=f_name[::-1]
rev_l=l_name[::-1]
print(rev_f+ ' '+rev_l)


# ### 3. Write a Python program to find the volume of a sphere with diameter 12 cm.

# In[15]:


def sphere_vol():
    d=12
    V=(4/3)*3.14*(d/2)**3
    return V
sphere_vol()
    


# In[ ]:




