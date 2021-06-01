#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ternary operator

a = 30
b = 20

min_value = a if a < b else b
print(min_value)


# In[4]:


a,b = 10,20

min_value = a if a < b else b
print(min_value)


# In[16]:


months = {"January": 1, "February":2, "March": 3, "April":4}

print(len(months))
print(months["January"])
print(months)
print()

print(months.items())
print(list(months.items()))
print(list(months.keys()))
print(list(months.values()))


# In[17]:


months = {"January": 1, "February": 2, "March": 3, "April": 4}

for month_name in sorted(months.keys()):
    print(month_name, end=" ")


# In[23]:


months = {"January": 1, "February": 2, "March": 3, "April": 4}

search_key = input("Enter your search key: ")

if search_key in months:
    print("The value of the search key is", months[search_key])
else:
    print("The search key is not in your dictionary")


# In[25]:


# get the summation of all values from declared dictionary

def sum_of_values_dict(my_dict):
    my_sum = 0
    for item in my_dict.values():
        my_sum += item
        
    return my_sum

my_dictionary = {'A': 100, 'B': 200, 'C': 300}

print("The sum of all values of my dictionary is:", sum_of_values_dict(my_dictionary))


# In[ ]:




