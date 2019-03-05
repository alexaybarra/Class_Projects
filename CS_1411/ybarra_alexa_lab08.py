"""
Name: Alexa Ybarra
Course: CS 1411-502
Date: 10/29/2018

Problem:
Write Python code to do the following:
1. Write Python code that would write random numbers in the range of 1 to 500
   to a text file. Your code should ask for the user input of how many random
   numbers to generate.

2. Write another code that would read in the previously generated file and
   calulate the total and average of those numbers.
       - Your code should check for IOError exceptions when the file is opened
         for writing/reading
       - Your code should check for ValueError exceptions when items are read
         from the file are converted to number.
"""
#Problem 1
import random

try:
    fileout = open('RandomNum.txt', 'w')

    for i in range(int(input('How many random numbers do you want to insert?: '))):
                   line = str(random.randint(1,500))
                   fileout.write(line)
                   fileout.write('\n')
                   print(line)

    fileout.close()

#Problem 2

    filein = open('RandomNum.txt','r')


    integers = []
    for n in filein.read().split():
        integers.append(int(n))
    filein.close()

    size = len(integers)
    total = sum(integers)
    avg = total/size

    print('sum of all numbers: ' +str(total) + '\n')
    print('average of numbers: ' +str(avg) + '\n')

except IOError:
    print('IOError')
except ValueError:
    print('ValueError')
