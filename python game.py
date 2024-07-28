import random
x=0
#Rock Paper Scissors
def gameWin (comp,you):
    #if two value are equal,declare a tie
    if comp == you:
        return None
    #check all the possibilities when computer chose r
    elif comp=='r':
        if you=='p':
            return False
        elif you=='s':
            return True
    #check for all possibilities when chomputer chose p
    elif comp=='p':
        if you == 's':
            return False
        elif you=='r':
            return True
    #check for all possibilities when chomputer chose s
    elif comp=='s':
        if you == 'r':
            return False
        elif you=='p':
            return True
print("Comp Turn: Rock(r) Paper(p) Scissors(s)?")
randNo=random.randint(1, 3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='s'

you=input("Your Turn: Rock(r) Paper(p) Scissors(s)?")
a=gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
    print("Your score:",x)
elif a:
    print("You Win!")
    x=x+1
    print("Your score:",x)
else:
    print("You Lose!")
    print("Your score:",x)
    