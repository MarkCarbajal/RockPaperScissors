import random

# Print Rules
print(
    "Winning Rules of the Rock paper scissor game as follows: \n"
    + "Rock vs paper->paper wins \n"
    + "Rock vs scissor->Rock wins \n"
    + "paper vs scissor->scissor wins \n"
)

Stop_play = False

while Stop_play is False:
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
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "paper"
    else:
        choice_name = "scissor"

    # print user choice

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value

    # Will always tie the game
    while comp_choice != choice:
        comp_choice = random.randint(1, 3)

    # initialize value of comp_choice_name
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "paper"
    else:
        comp_choice_name = "scissor"

    # print the computers choice, following by
    # your choice and your opponent(the computers) choice

    # condition for USER winning
    if choice == 2 and comp_choice == 1:  # Paper beats rock
        # print("paper wins => ", end = "")
        result = "paper"
        winner = "user"

    elif choice == 1 and comp_choice == 3:  # Rock beats scissors
        # print("rock wins =>", end = "")
        result = "rock"
        winner = "user"
    elif choice == 3 and comp_choice == 2:  # Scissor beats paper
        # print("scissor wins =>", end = "")
        result = "scissor"
        winner = "user"

    # condition for COMPUTER winning
    if comp_choice == 2 and choice == 1:  # Paper beats rock
        # print("paper wins => ", end = "")
        result = "paper"
        winner = "computer"
    elif comp_choice == 1 and choice == 3:  # Rock beats scissors
        # print("rock wins =>", end = "")
        result = "Rock"
        winner = "computer"
    elif comp_choice == 3 and choice == 2:  # Scissor beats rock
        # print("scissor wins =>", end = "")
        result = "scissor"
        winner = "computer"

    # Condition for a DRAW
    if choice == comp_choice:
        winner = "draw"

    # Printing either user or computer wins
    print(f"You chose {choice_name}...")
    print(f"The computer chose {comp_choice_name}...")
    if winner == "user":
        print("Congratulations! You won!")
    elif winner == "computer":
        print("Sorry, you lost. Computer won. Better luck next time :(")
    else:
        print("It's a draw!")

    # if user input n or N then condition is True
    print("\n")
    play_again = input("Would you like to play again? [Y/N]")
    if play_again == "Y" or play_again == "y":
        Stop_play = False
    if play_again == "N" or play_again == "n":
        Stop_play = True


# after coming out of the while loop
# we print thanks for playing

print("\nThanks for playing")
