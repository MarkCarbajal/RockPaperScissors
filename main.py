import random
 
# Print Rules
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
 
while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
     
    # take the input from user
    choice = int(input("User turn: "))
 
    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value
     
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
         
 
    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
         
    # print user choice

 
    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)
     
    # looping until comp_choice value
    # is equal to the choice value

 
    # initialize value of comp_choice_name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    
    #print the computers choice, following by
    #your choice and your opponent(the computers) choice
         
 
    # condition for winning
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
         
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"
 
    # Printing either user or computer wins

 
 
    # if user input n or N then condition is True

     
# after coming out of the while loop
# we print thanks for playing

print("\nThanks for playing")
