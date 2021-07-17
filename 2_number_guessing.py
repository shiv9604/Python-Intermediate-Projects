# Number Guessing Game
import random

comp_turn = random.randint(1,100)
print(comp_turn)
# no_of_userguess = 0

userguess = 0+1
while(userguess !=comp_turn):

    user_turn = int(input("\nPlease enter the guessed number : "))

    if user_turn>comp_turn:
        print("You guessed it wrong,Lower Number please")

    elif user_turn<comp_turn:
        print("You guessed it wrong,Higher Number please")

    else:
        print("\nCongratulations! You guessed it Correct...")
        print(f"You guessed the number correctly in {userguess} th attempt...\n")
        break
    userguess +=1

with open("number_guessing_hscore.txt","r") as f:
    highscore = int(f.read())

if(userguess<highscore):
    print(f"You just Created Highest score is : {userguess}!")
    with open("number_guessing_hscore.txt","w") as f:
        f.write(str(userguess))


