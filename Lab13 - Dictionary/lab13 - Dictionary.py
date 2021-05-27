#!/usr/bin/env python
# coding: utf-8

# In[12]:


# simple quiz game

counter = 0
questions = ["What is the capital of France? ","Which character is the most popular character of Walt Disney? "]
answers = ["paris","mickey mouse"]

for ques in questions:
    user_input = input(ques)
    user_input = user_input.lower()
    if user_input in answers:
        counter += 1
        print("Correct\n")
    else:
        print("Wrong\n")
        
print(f"Total correct is: {counter}")


# In[1]:


# transpose of matrix

import random

def print_matrix(nums):
    for row in nums:
        for item in row:
            print(item, end=" ")
        print()

row = 4
column = 3 
nums = [[random.randrange(10,30) for x in range(row)] for y in range(column)]

print("Original matrix:")
print_matrix(nums)
    
# len(nums[0]) stands for num of elements in first row
# len(nums[:]) stands for total num of row means how many elements in one column
new_nums = [[nums[row][column] for row in range(len(nums[:]))] for column in range(len(nums[0]))]

print("\nTranspose of matrix:")
print_matrix(new_nums)


# In[63]:


# sum of rows and columns of matrix
# total num of row means how many elements in one column
# total num of column means how many elements in one row
# nums[row][column]

nums = [[52,33,65,46],[36,27,84,17],[13,25,88,42]]

# prints the whole matrix
for row in nums:
    for item in row:
        print(item,end=" ")
    print()

print("---------------------")
for i,row in enumerate(nums):
    sumRow = 0
    for j,item in enumerate(row):
        sumRow += nums[i][j]
    print("sum of " + str(i + 1) + " rows " + str(sumRow)) 
    
print("---------------------")
for column in range(len(nums[0])): 
    # len(nums[0]) stands for num of elements in first row
    sumColumn = 0
    for row in range(len(nums[:])): 
        # len(nums[:]) stands for total num of row means how many elements in one column
        sumColumn += nums[row][column]
    print("sum of " + str(column + 1) + " columns " + str(sumColumn))


# In[89]:


# dictionary

dic = {1: "apple" , 2: "banana"} # mutable

print(dic[1])
print(dic)

dic[1] = "watermelon"
print(dic)

dic[3] = "orange"
print(dic)

del dic[2]
print(dic)


# In[91]:


d = {"dog": "has a tail and goes woof!", "cat": "says meow", "mouse": "chased by cat"}

word = input("Enter a word: ")

print("The definition is:", d[word])


# In[2]:



points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2, 'H':4,'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1, 'O':1, 'P':3,'Q':10, 'R':1, 'S':1, 'T':1, 'U':1, 'V':4, 'W':4, 'X':8,'Y':4, 'Z':10}

word = input("Enter your word: ")
word = word.upper()

score = sum([points[char] for char in word])
print(score)


# In[5]:


# concetnate dictionaries
dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}
dic4 = {}

for d in (dic1,dic2,dic3):
    dic4.update(d)
    
print(dic4)
print(len(dic4))


# In[4]:


fruits = {"apple": 1, "banana" : 2}

if "orange" in fruits:
    print("has orange")
else:
    print("no orange")


# In[18]:


# Dictionary Comprehension

squares = {x: x*x for x in range(6)}

print(squares)


# In[13]:


odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

print(odd_squares)
print(1 in odd_squares)
print(2 not in odd_squares)
print(49 in odd_squares) # only key not value


# In[17]:


odd_squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

for i in odd_squares:
    print(odd_squares[i],end = " ")


# In[ ]:




