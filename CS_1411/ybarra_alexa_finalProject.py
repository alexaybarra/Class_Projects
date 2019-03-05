"""
Name: Alexa Ybarra
Course: CS 1411-502
Date: 11/22/2018

Problem:
Write Python code to do the following:

    1. Database creation:
       You would create a file that would contain UserId (some unique number, you
       may use random number generator and this number should be used for looking
       up a specific user), Last name, First Name, Age (you can have a numeric
       value), Gender, City, Job, Interest/Hobby (one hobby or interest should be
       good; however, you can have multiple hobbies for one person) and contact
       (some chat id or email or phone). Please create at least 15-20 records.

    2. Finding matching buddy:
       Provide your users with two types of match options: location and
       interest/hobby. Show results based on the selection.
       
    3. Your code should be menu driven. First time it should have two option:
        a. Login
        b. Join (this should allow a new user to join).
        
       Next your code should allow the user with:
        c. Find a match
            i. Based on location
            ii. Based on insterests
            
    4. Proper exception handling.
    
    5. Code commenting.

"""
import csv
import sys

#initial creation of file
filetest = open('BuddyMatch.csv', 'r')
filetest.close()

try:
    
    print("\nWelcome to the Buddy Matching Program!\nWhat would you like to do?")

    #defining my menu
    def login_menu():
        print("\nMENU")
        print("(l)ogin")
        print("(j)oin")
        print("(e)xit")

        good_menu_choice = False

        #will make sure that the user is inputting the correct input for login, join, or exit
        while not good_menu_choice:
            Lchoice = input("Menu choice [l, j, e]: ")
            if Lchoice != 'l' and Lchoice != 'j' and Lchoice != 'e':
                print(Lchoice, " is invalid. Please try again.")
            else:
                good_menu_choice = True
        return Lchoice

    done = False
    while not done:
        user_login_choice = login_menu()

        #if user_login_choice = l, log the user in

        if user_login_choice == 'l' or user_login_choice == 'L':
            #read from CSV
            fileIn = open("BuddyMatch.csv", "rt")
            csvIn = csv.reader(fileIn, delimiter = ',')

            fileIn.seek(0)

            user_id = str(int(input("\nEnter Your User ID: ")))

            for row in csvIn:
                if user_id == row[0]:
                    print ("\nName: " + str(row[2]) + " " + str(row[1]) + "\nAge: " + str(row[3]) + "\nGender: " + str(row[4]) + "\nCity: " + str(row[5]) + "\nJob: " + str(row[6]) + "\nInterest: " + str(row[7]) + "\nEmail: " + str(row[8]))
                    user_city = row[5]
                    user_interest = row[7]
                    break

            #defining the menu for user to choose what they would like to search by
            def search_choice():
                print("\nWhat Would You Like To Search By:")
                print("(c)ity")
                print("(i)nterest")
                print("(e)xit")

                good_choice = False
                fileIn.seek(0)

                while not good_choice:
                    Schoice = input('Choice [c, i, e]: ')
                    if Schoice != 'c' and Schoice != 'i' and Schoice != 'e':
                        print(Schoice + " is not valid. Please try again.")
                    else:
                        good_choice = True
                return Schoice

            finished = False

            while not finished:
                user_choice = search_choice()
                buddy_found = False

                fileIn.seek(0)

                if user_choice == 'c' or user_choice == 'C':
                    #search for users with same city
                    for row in csvIn:
                        if  user_id != row[0] and user_city == row[5]:
                            buddy_found = True
                            print ("\nName: " + str(row[2]) + " " + str(row[1]) + "\nAge: " + str(row[3]) + "\nGender: " + str(row[4]) + "\nCity: " + str(row[5]) + "\nJob: " + str(row[6]) + "\nInterest: " + str(row[7]) + "\nEmail: " + str(row[8]))
                    if not buddy_found:
                        print("\nSorry, we could not find a buddy in your city. Please try another option, or exit!")

                if user_choice == 'i' or user_choice == 'I':
                    #search for users with same interests
                    for row in csvIn:
                        if user_id != row[0] and user_interest == row[7]:
                            buddy_found = True
                            print ("\nName: " + str(row[2]) + str(row[1]) + "\nAge: " + str(row[3]) + "\nGender: " + str(row[4]) + "\nCity: " + str(row[5]) + "\nJob: " + str(row[6]) + "\nInterest: " + str(row[7]) + "\nEmail: " + str(row[8]))
                    if not buddy_found:
                        print("\nSorry, we could not find a buddy with your interest. Please try another option, or exit!")

                if user_choice == 'e' or user_choice == 'E':
                    #exit program
                    fileIn.close()
                    print("\nLogging you out now! Goodbye!")
                    finished = True

        #end of Login

        #if user_login_choice = j, create a new account

        if user_login_choice == 'j' or user_login_choice == 'J':
            #read from CSV
            fIn = open("BuddyMatch.csv", "rt")
            csv_In = csv.reader(fIn, delimiter = ',')

            fIn.seek(0)

            id_num = 0

            for row in csv_In:
                id_num = id_num + 1

            fIn.close()

            #write to CSV

            print("Your ID Number is ", id_num)

            lname = input("Enter your last name: ")
            fname = input("Enter your first name: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender (male, female, other): ")
            city = input("What city do you live in? ")
            job = input("What is your job? ")
            interest = input("What is an interest of yours? ")
            email = input("Enter your email address: ")

            userData = [id_num, lname, fname, age, gender, city, job, interest, email]

            fOut = open("BuddyMatch.csv", "a", newline='')
            csvOut = csv.writer(fOut, delimiter = ',')

            csvOut.writerow(userData)

            fOut.close()

        #end of Join

        #exit
        if user_login_choice == 'e' or user_login_choice == 'E':
            #exit program
            print("\nThank you for using the program. Goodbye!")
            done = True
            exit()
            
#will print either IOError or ValueError if an error is found
except IOError:
    print ('IOError!')
except ValueError:
    print('ValueError!')
