import random
x=0
y=0
#Rock Paper Scissors
def gameWin (computer,you):
    #if two value are equal,declare a tie
    if computer == you:
        return None
    #check all the possibilities when computer chose r
    elif computer == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    #check for all possibilities when computer chose p
    elif computer == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    #check for all possibilities when c omputer chose s
    elif computer == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
z="yes"
while z=="yes":
    print("Computer Turn: Rock(r) Paper(p) Scissors(s)?")
    randNo=random.randint(1, 3)
    if randNo==1:
        computer='r'
    elif randNo==2:
        computer='p'
    elif randNo==3:
        computer='s'
    you=input("Your Turn: Rock(r) Paper(p) Scissors(s)?")
    a=gameWin(computer, you)
    print(f"Computer chose {computer}")
    print(f"You chose {you}")
    if a == None:
        print("The game is a tie!")
        print("Your score: ",x)
        print("Computer score: ",y)
    elif a:
        print("You Win!")
        x=x+1
        print("Your score: ",x)
        print("Computer score: ",y)
    else:
        print("You Lose!")
        y+=1
        print("Your score: ",x)
        print("Computer score: ",y)
    z=input("Do you still want to continue?(yes/no): ")
