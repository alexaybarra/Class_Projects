"""
Name: Alexa Ybarra
Course: CS 1411-502
Date: 10/01/2018

Problem:
Write Python code to do the following:

1. Write a Python program that accepts a word from the user and reverse it. (3 pts)

    E.g.: Enter a word: Hello
          The reverse: olleH

2. Write a Python program to guess a number between 1 to 9. (3 pts)
    Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears
    again until the guess is correct, on successful guess, user will get a "Well guessed!" message,
    and the program will exit.

    Hint: import random and use the randint function.

3. Write a Python program which iterates the integers from 1 to 50. For multiples of three
    print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
    which are multiples of both three and five print "FizzBuzz". (4 pts)

    Sample Output :
    fizzbuzz
    1
    2
    fizz
    4
    buzz


"""
#Problem 1
userInput_reverse_str = input('Enter a string to reverse: ')
print (userInput_reverse_str[::-1])


#Problem 2
number = 7
guess = int( input('Guess a number: '))
guessed = False

while 1 <= guess <= 9 and not guessed:
    if guess > number:
        print('Guessed too high.')
    elif guess < number:
        print('Guessed too low.')
    else:
        print('Well guessed!')
#        break
        guessed = True
    if not guessed:
        guess = int(input('Guess a number: '))


#Problem 3
for num in range(50):
    if num % 3 == 0 and num % 5 ==0:
        print('fizzbuzz')
        continue
    elif num % 3 == 0:
        print('fizz')
        continue
    elif num % 5 == 0:
        print('buzz')
        continue
    print(num)




       
