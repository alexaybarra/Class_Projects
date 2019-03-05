"""
Name: Alexa Ybarra
Course: CS 1411-502
Date: 11/5/2018

Problem:
Write Python code to do the following:

Write Python program for The Sprigfork Amateur Gold Club to do the following:
    a. A program that will read each player's id, name and golf score as
       keyboard input and then save all the records to a file named golf.txt
    b. Display all the records saved to golf.txt

Instructions:
    a. Make a menu driven program to create/add new players info
    b. View the players info
    c. Handle necessary exceptions
"""
import ast

try:
    fileout = open('golf.txt', 'r')
    fileout.close()

    def menu_choice():
        print('\nMENU')
        print('(c)reate/add new player info')
        print('(v)iew player info')
        print('(e)xit')

        good_menu_choice = False
        while not good_menu_choice:
            choice = input('Menu choice [c,v,e]: ')
            #if not any of the variables listed, print try again
            if choice != 'c' and choice != 'v' and choice != 'e':
                print(choice, 'is invalid- please try again')
            else:
                good_menu_choice = True
        return choice

    #Introduce program
    print('Welcome to The Sprigfork Amateur Gold Club program!')

    
    done = False
    while not done:
        user_menu_choice = menu_choice()
        # if choice c, create/add new player info
        if user_menu_choice == 'c':
            filein = open('golf.txt', 'a')

            player_id = str(int(input("Enter player's id: ")))

            player_name = str(input("Enter player's name: "))

            player_golf_score = str(int(input("Enter player's golf score: ")))

            dict = {player_id: player_name, player_name: player_golf_score}
            filein.write(str(dict))
            filein.write('\n')

            filein.close()
            print('File has been updated')

        # if choice v, view player info
        elif user_menu_choice == 'v':

            id_input = str(input("Enter Player's ID Number for viewing: "))
            filein = open('golf.txt', 'r')
            for line in filein:
                # ast.literal_eval(line) converts each line of the file and turns it from a String to a type 'Dictionary'. That way you can use the .get(key) method
                if ast.literal_eval(line).get(id_input) != None:
                    name = ast.literal_eval(line).get(id_input)
                    print ("Player Name  : " + name)
                    score = ast.literal_eval(line).get(name)
                    print ("Player Score : " + score)
                    break
                if line == "":
                    print("No ID was found")
            
            filein.close()
            print('File is now closed')

        # if choice e, exit menu
        elif user_menu_choice == 'e':
            # done is changed to True since the user no longer wants to use the program
            done = True
            print('Thank You!')
            exit()


except IOError:
    print('IOError')
except ValueError:
    print('ValueError')

