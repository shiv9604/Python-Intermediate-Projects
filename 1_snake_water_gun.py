# programme for Rock Scissor Paper game in python.
import random

def Gamewin(comp,you):
    # IF both puts the same input then Game wil tie.
    if comp == you:
        return None
    #Check all possibilities for the loosing and winning conditions.
    elif comp == 's':
        if you =='p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you =='r':
            return False
        elif you == 's':
            return True
    elif comp == 'r':
        if you =='s':
            return False
        elif you == 'p':
            return True

#Computer's Turn starts here.
print("Comp turn : Scissor(s),Paper(p),Rock(r) ?")
rand_number = random.randint(1,3) # --> random can choose only int and you have to convert that input into usefull string.
if rand_number == 1:
     comp = 's' 
elif rand_number == 2:
     comp = 'p'
elif rand_number== 3:
     comp = 'r' 

#Your Turn starts here.
you =  input("Your Turn : Scissor(s),Paper(p),Rock(r) ? : ")
a = Gamewin(comp,you)

#This will tell us what computer choosed and what you choosed
print(f"computer choosed : {comp}")
print(f"You choosed : {you}")

#This will tell us We won or loosed.
if a == None:
    print("Game is tie.")
elif a:
    print("You win.")
else:
    print("You Loose")
