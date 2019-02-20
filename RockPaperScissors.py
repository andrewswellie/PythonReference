 # Incorporate the random library
import random
restart = 1

while restart != "x":
    
    print("Let's Play Rock Paper Scissors!!!")
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)
    user_choice = input("You are playing against the computer. His choice is completely random. Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    
    if (user_choice == "r") and (computer_choice == "p"):
        print("You Lose.")
        restart = input("press any key to start again, or x to exit.") 
    elif (user_choice == "p") and (computer_choice == "s"):
        print("You Lose.")
        restart = input("press any key to start again, or x to exit.") 
    elif (user_choice == "s") and (computer_choice == "r"):
        print("You Lose.")
        restart = input("press any key to start again, or x to exit.") 
                    
    if (user_choice == "s") and (computer_choice == "p"):
        print("You WIN!!!")
        restart = input("press any key to start again, or x to exit.") 
    elif (user_choice == "r") and (computer_choice == "s"):
        print("You WIN!!!")
        restart = input("press any key to start again, or x to exit.") 
    elif(user_choice == "p") and (computer_choice == "r"):
        print("You WIN!!!")
        restart = input("press any key to start again, or x to exit.") 
                    
    if (user_choice == computer_choice):
        print("TIE! Kind of like kissing your sister. Try again.")
        restart = input("press any key to start again, or x to exit.") 
  