#!/usr/bin/env python
# coding: utf-8

# In[42]:


for i in range(1,11):
    print("*"*i)


# In[11]:


for i in range(1,11):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


# In[10]:


for i in range(1,11):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[26]:


for i in range(10, 0, -1):
    for j in range(0, i):
        print("*",end=" ")
    print()    


# In[30]:


for i in range(11, 1, -1):
    for j in range(1, i):
        print(j,end=" ")
    print()


# In[60]:


less_count = int(input("How many drink containers 1 liter or less do you have? "))
more_count = int(input("How many drink containers more than 1 liter do you have? "))

less = less_count * 0.10
more = more_count * 0.25
total = more + less

print("\nFor 1 liter or less:", format(less, ".2f"),"$")
print("For more than 1 liter:", format(more, ".2f"),"$")
print("\nTotal:", format(total, ".2f"),"$")
print("Your total refund will be $%.2f" %total)


# In[67]:


'''
toonie = 200 cents
loonie = 100 cents
quarter = 25 cents
dime = 10 cents
nickel = 5 cents
pennies = 1 cent

'''

money = int(input("Enter your amount of money in cents: "))

toonie = 200 
loonie = 100 
quarter = 25 
dime = 10 
nickel = 5 
pennie = 1

toonie_count = money // toonie
money = money % toonie

loonie_count = money // loonie
money = money % loonie

quarter_count = money // quarter
money = money % quarter

dime_count = money // dime
money = money % dime

nickel_count = money // nickel
money = money % nickel

pennie_count = money // pennie

print("Toonies: ",toonie_count)
print("Loonie: ",loonie_count)
print("Quarter: ",quarter_count)
print("Dime: ",dime_count)
print("Nickel: ",nickel_count)
print("Pennies:",pennie_count)


# In[69]:


'''
toonie = 200 cents
loonie = 100 cents
quarter = 25 cents
dime = 10 cents
nickel = 5 cents
pennies = 1 cent

'''

money = int(input("Enter your amount of money in cents: "))

toonie = 200 
loonie = 100 
quarter = 25 
dime = 10 
nickel = 5 
pennie = 1

print(money // toonie,"toonies")
money = money % toonie

print(money // loonie,"loonies")
money = money % loonie

print(money // quarter,"quarters")
money = money % quarter

print(money // dime,"dimes")
money = money % dime

print(money // nickel,"nickels")
money = money % nickel

print(money // pennie,"pennies")


# In[ ]:




