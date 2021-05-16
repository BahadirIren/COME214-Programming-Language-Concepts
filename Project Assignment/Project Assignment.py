#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1
# imported randint from random in order to generate random numbers
from random import randint

# defined function called game and accepts computer choice as a paramater
def game(computer_choice):
    # 0 means computer chose Rock
    if computer_choice == 0:
        
        # checks whether user choice and computer choice is equal or not
        if user_choice == "rock":
            # if true then tie will be printed
            print("Tie")
            
        # computer already chose rock and checks whether user won or not 
        elif user_choice == "paper":
            # if true then user won and message printed
            print("Paper covers rock, You won")
            
        # computer already chose rock and checks whether user won or not     
        elif user_choice == "scissors":
            # if true then user lost and message printed
            print("Rock crushes scissors, You lost")
            
    # 1 means computer chose Paper
    elif computer_choice == 1:
        
        # checks whether user choice and computer choice is equal or not
        if user_choice == "paper":
            # if true then tie will be printed
            print("Tie")
        
        # computer already chose paper and checks whether user won or not 
        elif user_choice == "rock":
            # if true then user lost and message printed 
            print("Paper covers rock, You lost")
        
        # computer already chose paper and checks whether user won or not 
        elif user_choice == "scissors":
            # if true then user won and message printed
            print("Scissors cut paper, You won")
            
    # 2 means computer chose Scissors       
    elif computer_choice == 2:
        
        # checks whether user choice and computer choice is equal or not
        if user_choice == "scissors":
            # if true then tie will be printed
            print("Tie")
        
        # computer already chose scissors and checks whether user won or not 
        elif user_choice == "rock":
            # if true then user won and message printed
            print("Rock crushes scissors, You won")
        
        # computer already chose scissors and checks whether user won or not 
        elif user_choice == "paper":
            # if true then user lost and message printed
            print("Scissors cut paper, You lost")
        
# declared a boolean variable to store game status (game is finished or not)
# assigned False value in order to loop once and check whether game is finished or not
is_finished = False
# loop continue until is_finished is True this means loop continue until game is finished
while not is_finished:
    
    # each time computer chose random number from 0,1,2
    computer_choice = randint(0,2)
    
    # asks user to enter Rock, Paper or Scissors if user enters 1 game is finished
    user_choice = input("\nWrite Rock, Paper or Scissors (Enter 1 for exit): ")
    # in order to accept upper case letter we should transform input to lower case 
    user_choice = user_choice.lower()
    
    # if user enters 1 this means game is finished
    if user_choice == "1":
        # we should set is_finished to True in order not to execute while loop anymore
        is_finished = True
        # message will be printed
        print("Game is finished!")
    
    # if user enters valid input then call the function
    elif user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        # calls the function with computer choice as a paramater
        game(computer_choice)
    
    # in this case user entered invalid input
    else:
        # informs that user entered invalid input
        print("Invalid input entered! ")
         


# In[2]:


# 2

# defined function called sort_list and accepts list as a paramater
def sort_list(list):
    # loop the list from beginning to end
    for i in range(len(list)):
        # loop the list from i+1 index to end
        for j in range(i + 1, len(list)):
            # if list[i] is bigger than list[j]
            if list[i] > list[j]:
                # then swap the values
                list[i],list[j] = list[j],list[i]
    
    # in the end returned the list
    return list

# asks user to enter size of the list
size_of_list = int(input("Enter the total number of list elements: "))
# creates empty list
list = []

# iterates size of the list times
for i in range(size_of_list):
    # asks user to enter list item and adds the value at the end of the list
    list.append(int(input(f"Enter the value of {i + 1} element: ")))

# prints the whole list before the sort_list called (prints original list)
print("\nElements before sorting the list: ", list[:])
# prints the whole sorted list in ascending order
print("Elements after sorting the list in ascending order is: ", sort_list(list))


# In[11]:


# 3 

# defined a variable in order to store text
corpus_original = ('''
“Doubt thou the stars are fire;
Doubt that the sun doth move;
Doubt truth to be a liar; 
But never doubt I love.”''')

# converted text to lower case in order to produce right output
corpus_lower = corpus_original.lower()
# asks user to enter subtext
subtext = input("Enter subtext: ")
# converted text to lower case in order to produce right output
subtext = subtext.lower()
# splits text word by word and puts in a list
corpus_splitted = corpus_lower.split()

# in order to keep track of the frequency, defined variable and set it to 0
frequency = 0
# iterates length of the list item
for i in range(len(corpus_splitted)):
    # chekcs whether entered subtext is in the list or not
    if subtext in corpus_splitted[i]:
        # if it exists in the list then increment frequency by one
        frequency += 1

# prints the original text
print("\nThe original text is:", corpus_original)
# prints the entered subtext
print("\nThe subtext is:", subtext)
# prints the frequency of the entered subtext
print("The frequency of subtext in Corpus is:", frequency)


# In[21]:


# 4

# imported random in order to generate random numbers
import random

# defined function called roll_dice
def roll_dice():
    # created dice variables with random number between 1 to 6
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    # function returns sum of these dice faces
    return dice1 + dice2


# called roll_dice function and assigned to sum_of_dice_face variable
sum_of_dice_face = roll_dice()
# printed the sum of dice faces
print("The sum of dice 1 and dice 2:", sum_of_dice_face)

# if sum_of_dice_face is equal to 7 or 11 on the first throw
if sum_of_dice_face == 7 or sum_of_dice_face == 11:
    # if true then user won and game is finished
    print("You won, game is finished!")

# if sum_of_dice_face is equal to 2 or 3 or 12 on the first throw
elif sum_of_dice_face == 2 or sum_of_dice_face == 3 or sum_of_dice_face == 12:
    # if true then user lost and game is over
    print("You lost, game over!")

# if those conditions are not true then else part will be executed
else:
    # assigned sum_of_dice_face to point
    point = sum_of_dice_face
    # continue loop until it breaks
    while True:
        # rolled the dice again 
        print("\nRolling dice...")
        # called roll_dice function and assigned to sum_of_dice_face variable
        sum_of_dice_face = roll_dice()
        
        # if point is equal to sum_of_dice_face without getting sum_of_dice_face is equal to 7
        if point == sum_of_dice_face:
            # printed the sum of dice faces
            print("The sum of dice 1 and dice 2:", sum_of_dice_face)
            # if true then user won and game is finished
            print("You won, game is finished!")
            # in order to exit the loop
            break
        
        # otherwise, if sum_of_dice_face is equal to 7
        elif sum_of_dice_face == 7:
            # printed the sum of dice faces
            print("The sum of dice 1 and dice 2:", sum_of_dice_face)
            # if true then user lost and game is over
            print("You lost, game over!")
            # in order to exit loop
            break
        
        # otherwise
        else:
            # printed the sum of dice faces
            print("The sum of dice 1 and dice 2:", sum_of_dice_face)


# In[28]:


# 5 

# in order to handle the wrong input
try:
    # asks user to enter age
    age = int(input("Enter your age: "))
    # iterates until entered age is positive
    while age < 0:
        # inform user to enter positive number
        print("Age must be positive number!")
        # assign new age number to age variable
        age = int(input("Enter your age: "))
        
    # else case means entered number is positive
    else:
        # if age is less than or equal to 19
        if age <= 19:
            # informs users that they are eligible for student discount
            print("Eligible for a student discount")
            
        # if entered age is bigger than or equal to 65    
        elif age >= 65:
            # informs users that they are eligible for senior discount
            print("Eligible for a senior discount")
        
        # otherwise
        else:
            # informs user that they are not eligible for discount
            print("Not eligible for a discount")
            
# if user enters invalid input, except handles and application won't produce error
except:
    # informs user that they entered invalid input
    print("Invalid input, Age must be integer number!")


# In[245]:


# 6

# defined function called decimal_to_base and accepts number and base as a parameters
def decimal_to_base(number, base):
    # created result variable and initialized to empty string
    result = ""
    
    # iterates as long as the number is positive
    while number > 0:
        # does number modulus base operation and puts remainder to remainder variable
        remainder = number % base
        # adds remainder part to the result string
        result += str(remainder)
        # does number divided by base and ignored after the dot part
        number = number // base
        
    # reversed the string
    result = result[len(result)::-1]
    
    # function returns the result
    return result

# asks user to enter decimal number
decimal_number = int(input("Enter a decimal number: "))
# asks user to enter base number between 2 and 16
base = int(input("Enter a base number between 2 and 16: "))

# if entered base number is invalid
if base < 2 or base > 16:
    # informs user that they are entered invalid base number
    print("\nInvalid base number entered!, must be between 2 to 16")

# otherwise entered base number is valid
else:
    # prints the converted result
    print(f"\nThe decimal number {decimal_number} to base {base} is:",decimal_to_base(decimal_number, base))


# In[9]:


# 7

# created text list and initialize with A, B, C values
text = ['A','B','C']

# checks whether list items are equal to each other or not
if text[0] != text[1] and text[1] != text[2]:
    
    # iterates until the length of the list
    for i in range(len(text)):
        
        # iterate 1 to length of the list
        for j in range(1,len(text)):
            # if j is equal to length of the list -1
            if j == len(text)-1:
                # if true then swap list items
                text[1],text[2] = text[2],text[1] 
            
            # prints the result
            print("".join(text[i:]+ text[:i]))

# otherwise there is some list items are equal to each other
else:
    # informs user that some list items are equal to each other
    print("Some list items are equal to each other")
                 


# In[29]:


# 8 

# imported string in order to use standart string library
import string

# defined function called convert_text and accepts text as a parameter
def convert_text(text):
    # removed blanks in the text
    text = text.replace(" ", "")
    # converted text into lower case
    text = text.lower()
    
    # in case there is a punctuation in the text, 
    # loop every elements of the string.punctuation
    for punctuation in string.punctuation:
        # removed punctuation in the text
        text = text.replace(punctuation , "")
    
    # function retruns text
    return text

# asks user to enter text
text_original = input("Enter a text: ")
# called function and passed text_original as a parameter
# function result will be stored in the text variable
text = convert_text(text_original)

# if normal text and reversed text is equal to each other
# text[len(text)::-1] this mean we reversed the text
if text == text[len(text)::-1]:
    # if true then entered text is palindrome
    print(f"\n{text_original} is a palindrome")

# otherwise, normal text and reversed text is not eqaul to each other
else:
    # if true then entered text is not palindrome
    print(f"\n{text_original} is not a palindrome")


# In[32]:


# 9 

# defined a function called compare_strings and accepts two string variables as parameters
def compare_strings(string1, string2):
    # if the length of the string1 is greater than string2
    if len(string1) > len(string2):
        # if true then length of the string1 is longer
        # printed string1
        print(string1)
        
    # if both length of the strings are eqaul
    elif len(string1) == len(string2):
        # printed both of them
        print(string1)
        print(string2)
    
    # otherwise, the length of the string2 is greater than string1
    else:
        # if true then length of the string2 is longer
        # printed string2
        print(string2)

# asks user to enter string1
string1 = input("Enter first string: ")
# asks user to enter string2
string2 = input("Enter second string: ")

# called function and passed strings as parameters
compare_strings(string1,string2)


# In[213]:


# 10

# asks user to enter a year
year = int(input("Enter a year: "))

# if entered year is divisible by 4 and not divisible by 100 or entered year is divisible by 400 
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    # if true then entered year is leap year
    # printed the result
    print(f"{year} is leap year")

# otherwise
else:
    # entered year is not a leap year
    # printed the result
    print(f"{year} is not a leap year")


# In[ ]:




