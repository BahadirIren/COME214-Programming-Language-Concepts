#!/usr/bin/env python
# coding: utf-8

# In[34]:


Hey_Jude=['Hey', 'Jude', "don't", 'make', 'it', 'bad',
'Take', 'a', 'sad', 'song', 'and', 'make', 'it', 'better',
'Remember' ,'to', 'let', 'her', 'into', 'your', 'heart',
'Then' ,'you' ,'can' ,'start' ,'to' ,'make' ,'it' ,'better']

my_dict = {}

for word in Hey_Jude:
    my_dict[word] = Hey_Jude.count(word)

max_times = max(my_dict.values())
most_list = [word for word,times in my_dict.items() if times == max_times]

print(most_list ,",", max_times)


# In[43]:


# SET (immutable) every element is unique

empty_list = []
empty_dict = {}
empty_tuple = ()
empty_set = set()


# In[38]:


my_set = {1,2,3,4}
print(my_set)
print(type(my_set))

my_set = {1.0, "hello", (1,2,3)}
print(my_set)

my_set = {1,2,2,2,3,4,5,5,5,5}
print(my_set)


# In[66]:


color = {"orange","red","red", "pink","orange"}

print(color)
color.add("blue")
print(color)
color.remove("blue")
print(color)
print(sorted(set(color)))
color.pop()
print(color)
color.clear() # clears all the elements in the set
print(color)
print()

print(sorted("pyyyytttthoooonnnn"))
print(sorted(set("pyyyytttthoooonnnn"))) # duplicates not allowed in set
print()

print("red" in color)
print("purple" in color)
print("purple" not in color)


# In[52]:


color = {"orange","red","red", "pink","orange"}

for item in color:
    print(item.upper())


# In[57]:


numbers = list(range(10)) + list(range(5))
print(numbers)
print(type(numbers))
print(set(numbers))


# In[72]:


# list version
import random

my_list = [random.randrange(1,7) for i in range(50)]

print(my_list)
print()

# set version
my_set = set([random.randrange(1,7) for i in range(50)])

print(my_set)


# In[82]:


text = "to be or not to be that is the question"
print(text.split())
print()

unique_words = set(text.split())
print(unique_words)
print(sorted(unique_words))


# In[86]:


# union in set

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9,10}

print(A|B)
print(A.union(B))
print(B.union(A))


# In[89]:


# intersection of sets

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9,10}

print(A&B)
print(A.intersection(B))
print(B.intersection(A))


# In[93]:


# difference of two sets

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9,10}

print(A-B)
print(A.difference(B))
print(B-A)
print(B.difference(A))


# In[96]:


for letter in set("helloworld"):
    print(letter, end= " ")


# In[ ]:




