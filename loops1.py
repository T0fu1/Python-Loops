#----------------------------------------------------------------------#
#-------------------------WHILE LOOPS----------------------------------#
#----------------------------------------------------------------------#
'''
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
n = int(input("Enter a number: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n: #means while i is less than or equal to n
    sum = sum + i #this moves onto the next number
    i = i+1  #update counter

# print the sum
print("The sum is", sum)
'''
#----------------------------------------------------------------------#
'''
#Example to illustrate
#the use of else statement
#with the while loop

number = int(input("Enter a number: "))
counter = 0

while counter < number: #while counter is less than your input
    print("Inside loop") #prints the amount you put as your input
    counter = counter + 1 #updates the counter
else:
    print("Inside else") #this is where is ends

print(counter) #shows the amount of counts it took
 '''   
#----------------------------------------------------------------------#
'''
#Python while loop with user input
a = int(input('Enter a number (-1 to quit): '))
  
while a != -1: #if a does not equal to -1, this makes the code keep going until the user enters -1
    a = int(input('Enter a number (-1 to quit): '))
    if a == -1:
        print("You just ended")
        break
'''
#-----------------------------------------------------------------------#
'''
#Guessing Game
import random
target = random.randint(1,10)
print('target = ', target, '\n')
numGuesses = 0
won = False

print('Instructions')
while numGuesses < 3 and won == False:
    currGuess = int(input('please guess a number between 1 and 10 \n'))
    numGuesses = numGuesses+1
    if currGuess == target:
        print('Congratualtions you won! Dance around and celebrate')
        won = True
if won == False:
    print('Sorry you lost, better luck next time.')
'''
#-----------------------------------------------------------------------#
#---------------------------FOR LOOPS-----------------------------------#
#-----------------------------------------------------------------------#
'''
#Simple For loop to print out all the letters in your input
sentence = input("Enter a sentence: ")

for i in sentence: #for every letter in your input sentence
    print(i) #They will go to i and prints out every letter in the terminal, including spaces because it's still a character
'''
#-----------------------------------------------------------------------#
'''
#Program to add numbers in a list using a while loop and then finding the sum of the numbers in the list you added using a for loop
myList = []
a = int(input("Enter a number to add (type -1 to stop): "))
myList.append(a)

while a != -1:
    a = int(input("Enter a number to add (type -1 to stop): "))
    myList.append(a)
    if a == -1:
        print("You stopped adding numbers.")
        myList.pop() #removes the last element(number) in the list (In this case -1 because -1 is still a number to be added in the list)
print("Here is your list: ", myList)

#Same code but adds all the numbers u added to your list
total = 0
for i in myList:
    print("Total sum of numbers in your list is: ",sum(myList))
    break
'''
#-----------------------------------------------------------------------#

