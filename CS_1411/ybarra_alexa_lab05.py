"""
Name: Alexa Ybarra
Course: CS 1411-502
Date: 10/8/2018

Problem:
Write Python code to do the following:

1. Define a string that contains a Python code to create and print a list where the values are
   square of numbers between 1 and 30 (both included). Now, execute this string through
   another Python function. (3pts)

2. Write a Python function to check whether a number is perfect or not. (4pts)

    According to Wikipedia : In number theory, a perfect number is a positive integer that is
    equal to the sum of its proper positive divisors, that is, the sum of its positive divisors
    excluding the number itself. Equivalently, a perfect number is a number that is half the sum
    of all of its positive divisors (including itself).

    Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors,
    and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive
    divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is
    followed by the perfect numbers 496 and 8128.

3. Write a Python program that accepts a hyphen-separated sequence of words as input and
   prints the words in a hyphen-separated sequence after sorting them alphabetically. (3pts)

   Example : Python-Java-C-Dotnet-MySQL
   Expected Result : C-Dotnet-Java-MySQL-Python


"""

#Problem 1

s= '''
def square_num():
    a = list()
    for i in range(0,31):
        a.append(i**2)
    print(a)
       # i = i + 1

square_num()
'''
#print(s)
exec(s)

#Problem 2
num = int(input('Enter a number to determine whether it is perfect or not: '))
if num >1:
    sum = 0
    for i in range(1,num//2+1):
        if num%i == 0:
            sum += i      
    if num == sum:
        print(num, 'is perfect')
    else:
        print(num, 'is not perfect')

#Problem 3
'''
.split('-') # used to split items
.join(items) # used to join items

seqwords = str(input('Enter a sequence of hyphen-separated words :'))
seqwords.split('-')
'''

seqwords = [n for n in (input('Enter a sequence of hyphen separated words :').split('-'))]
seqwords.sort()
print('-'.join(seqwords))
