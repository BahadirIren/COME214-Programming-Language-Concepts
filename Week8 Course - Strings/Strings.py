#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = "Hello"
t = 'hello'
m = """This is a long string this is
spread across two lines..."""

print(s)
print(t)
print(m)
print(type(m))


# In[4]:


my_string =input("Enter a string: ")
print(my_string)
print(type(my_string))


# In[10]:


print("Hello " + "Bahadir")
print("Hello " * 4)


# In[13]:


# Ask five times the user to enter a letter from keyboard
# the program should builds a string consist of vowels that are entered

s = ""
for i in range(5):
    ch = input("Enter a letter: ")
    ch = ch.lower() # converts all the letters to lowercase
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        s += ch

print(s)


# In[16]:


if "a" in "bahadir":
    print("Your string contains the letter a")
    
if "z" not in "bahadir":
    print("Your string not contains the letter z")


# In[18]:


s = ""
for i in range(5):
    ch = input("Enter a letter: ")
    ch = ch.lower() # converts all the letters to lowercase
    if ch in "aeiou":
        s += ch

print(s)


# In[29]:


# Indexing

s = "Python"
print(s[0])
print(s[-6])
print(s[-1])
print(len(s))
print(s)


# In[39]:


# Slices

s = "abcdefghij"
print(s[0:4])
print(s[:4]) # default 0
print()
print(len(s))
print()
print(s[2:len(s)])
print(s[2:]) # goes until at the end of the string
print()
print(s[:]) # print all the character in the string
print(s)
print()
print(s[1:7:2]) # starts with index 1 and skip 2 letter end with index 7
print()
print(s[::-1]) # a negative step reverses your string


# In[46]:


# prints whole string
s = "abcdefghij"
for i in range(len(s)):
    print(s[i],end="")
print()
for i in s:
    print(i,end="")
print()
print(s)


# In[52]:


s = "abcdefghiiiiiiiij"
print(s)
print(s.upper())
print(s)
s = s.replace('ab','AB')
print(s)
print(s.index("g"))
print(s.count("i"))


# In[58]:


# isalpha method is used to tell if character is a letter or not

s = input("Enter a string: ")
if s[0].isalpha():
    print("Your string is starts with a letter")
else:
    print("Your string doesnt start with a letter")


# In[66]:


dir(str)


# In[67]:


print("Hi\nthere")


# In[69]:


s = 'I can't go there'
print(s)


# In[68]:


s = 'I can\'t go there'
print(s)


# In[72]:


filename = "C:\\programs\\file.py"
print(filename)


# In[74]:


# write a program that asks for the user for a string and prints out the location of each "a" in the string

s = input("Enter some text: ")
for i in range(len(s)):
    if s[i] == "a":
        print(i)


# In[ ]:




