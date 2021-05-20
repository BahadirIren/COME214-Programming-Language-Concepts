#!/usr/bin/env python
# coding: utf-8

# In[4]:


# print i as long as i less than 6

i = 1
while i < 6:
    print(i)
    i += 1


# In[5]:


# x < 10 , x = 3

x = 3
while x < 10:
    print(x)
    x += 1


# In[8]:


# find square of each number 1 to 10

i = 1
while i < 11:
    print(i**2)
    i += 1


# In[9]:


# break statement

i =1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1


# In[16]:


# continue statement

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# In[18]:


# else 

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
    


# In[25]:


# sum = 1+2+3+4....+n 

n = int(input("Enter a number: "))

sum = 0
while 0 < n:
    sum += n
    n -= 1
print("Sum of this series is",sum)


# In[27]:


# find even number 0 - 30 

even = 0
while even < 30:
    print(even,end=" ")
    even +=2
    


# In[36]:


# ask for starting and ending values from the user print all the odd numbers between starting to ending values

starting = int(input("Enter starting value: "))
ending = int(input("Enter ending value: "))

if starting > ending:
    print("Ending value should be greater than starting value!")
    
while starting < ending:
    if starting % 2 != 0:
        print(starting, end=" ")
    starting += 1


# In[40]:


# even, odd number 

x = 1
while x <= 10:
    if x % 2 == 1:
        print(f"number {x} is odd")
    else:
        print(f"number {x} is even")
    x += 1
    


# In[90]:


'''
A class of 10 students took a quiz. The grades (int 0 to 100). Calculate and display the total of all students
grades and the class average on the quiz

Alternative 1

'''

import random

students = []
num_students = 10

# filled the students list
i = 0
while i < num_students:
    students.append(random.randrange(0,101))
    i += 1

# calculate sum
sum = 0
i = len(students) - 1 
print("Grades:")
while i > 0:
    print(students[i],end=" ")
    sum += students[i]
    i -= 1
    
print("\n\nSum of all students grade is:", sum)
print("Average is:", sum/len(students))


# In[87]:


'''
A class of 10 students took a quiz. The grades (int 0 to 100). Calculate and display the total of all students
grades and the class average on the quiz

Alternative 2

'''

total = 0 
gradeCounter = 0
numOfStudents = 10

while gradeCounter < numOfStudents:
    grade = int(input(f"Enter student {gradeCounter + 1} grade: "))
    total += grade
    gradeCounter += 1

average = total / gradeCounter

print(f"Sum of {numOfStudents} students grade: ", total)
print(f"Average is:", format(average,".2f"))


# In[98]:


total = 0 
gradeCounter = 0

grade = int(input(f"Enter student {gradeCounter + 1} grade (enter -1 to exit): "))

while grade != -1:
    total += grade
    gradeCounter += 1
    grade = int(input(f"Enter student {gradeCounter + 1} grade (enter -1 to exit): "))
    
print("\nYou have entered", gradeCounter, "grade")

if gradeCounter != 0:
    average = total / gradeCounter
    print(f"Average is:", format(average,".2f"))
else:
    print("There is no grade")


# In[101]:



studentsCounter= 0
passedCounter = 0
failedCounter = 0

while studentsCounter < 10:
    status = int(input("Enter result (1 for passed, 2 for failed): "))
    if status == 1:
        passedCounter += 1
    else:
        failedCounter += 1
    
    studentsCounter += 1
    
print("\nNumber of students passed:", passedCounter)
print("Number of students failed:", failedCounter)
    
if passedCounter >= 8:
    print("Raise Tuition")


# In[ ]:




