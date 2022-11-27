import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:     
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='sc':
            return True
    
    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you=='sc':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose sc
    elif comp == 'sc':
        if you=='p':
            return False
        elif you=='s':
            return True

print("Comp Turn: Stone(s) Paper(p) or Scissor(sc)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'

you = input("Your Turn: Stone(s) Paper(p) or Scissor(sc)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")