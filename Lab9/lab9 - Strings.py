#!/usr/bin/env python
# coding: utf-8

# In[5]:


title = "wind in the the willows"
print(title.upper())
print(title.lower())
print(title.capitalize())
print(title)


# In[13]:


s = "   Hi, Hannah"
print(s.count(" "))
print(s.replace("Hi","Hello")) # replaces every occurance
print(s.index("a"))  # first occurance


# In[18]:


birth_year = "1988"
state = "LA"
print(birth_year.isdigit()) # returns true if string is consists of digit
print(state.isalpha())  # returns true if string is consists of letter


# In[23]:


first_name = ("   Hannah  ")
print(first_name.strip())  # removes all the blanks


# In[25]:


first_name = ("*******Hannah*****")
print(first_name.strip("*"))  # removes all the specific input
print(first_name.rstrip("*"))
print(first_name.lstrip("*"))


# In[31]:


s = "abcdefghij"
print(len(s))
print(s[0])
print(s[-2])
print(s[0:2])
print(s[1:7:2])


# In[34]:


s = "abcdefghij"

for i in s:
    print(i, end=" ")


# In[106]:


# example1: print 3 blank lines

for i in range(4):
    print("\n")
    
# print("\n"*4)


# In[60]:


# example2: Print the location of each "a" in the string
s = input("Enter a string: ")

for i in range(len(s)):
    if s[i] == "a":
        print(i, end=" ")


# In[69]:


# example3: Enter your string Qbert output will be Q*ert!!!

s = "Qbert"
s = s.replace("b","*")
s += "!!!"
print(s)
# print(s+"!!!")


# In[70]:


'''
example4: write a program that asks user for a string creates a new string that doubles each character
of the original string
'''

s = input("Enter a string: ")

for i in s:
    print(i*2,end="")


# In[84]:


'''
example5: write a program that asks a user for their name and prints it in the following pattern:
input: Elvis
output: E El Elv Elvi Elvis
'''

s = input("Enter your name: ")

for i in range(len(s)):
    print(s[:i+1], end=" ")


# In[99]:


# example6: write a program that contains decimal number, print out the decimal number if 3.1415 output: .1415

num = input("Enter a decimal number: ")
index = num.index(".")
print(num[index:])


# In[102]:


# unicode for pi: 03c0
print("i love my Raspbery \u03c0!")


# In[105]:


'''
given string
s1: America
s2: Japan
new string made of first, middle and last character each string
output: AJrpan
'''

s1 = "America"
s2 = "Japan"
s = ""

s += s1[0]
s += s2[0]

s += s1[(len(s1)//2)]
s += s2[(len(s2)//2)]

s += s1[-1]
s += s2[-1]
print(s)


# In[ ]:




