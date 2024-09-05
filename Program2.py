# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.

name = input("What is your name? ")
print(name)
print(name)



## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.

name = input("What is your name? ")
print("!" + name + "!" + name + "!")
## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630

firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
streetaddress = input("What is your street address? ")
postcode = input("What is your city and postal code? ")
print("Here is all your information together :)")
print(firstname)
print(lastname)
print(streetaddress)
print(postcode)
## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out

word1 = input("Enter your favorite word: ")
word2 = input("Enter your second favorite word: ")
word3 = input("Enter your third favorite word: ")
print(word1 + "-" + word2 + "-" + word3)
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.

name = input("Enter a name for your very own fictional character: ")
year = input("What year do you want him/her to be in? Enter a future year here: ")
print(name + " is a very tech-savvy individual, born in the year " + year + ".")
print("In a world filled with advanced technology and AI, " + name + " was known for their incredible skills.")
print("One day in the year " + year + ", " + name + " discovered a mysterious piece of technology.")
print("It had the power to change the world, and only " + name + " knew how to unlock its potential.")