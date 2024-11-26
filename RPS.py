from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
#set player to Ture
 player = input('Rock, Paper, Scissors?')
if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("you lose!", computer, "covers", player)
    else:
        print("you win!", player, "smashes", computer)
elif player == "Paper":
    if computer == "Scissors":
        print("you lose!", computer, "cut", player)
    else:
        print("you lose!", player, "covers", computer)
elif player == "Scissors":
    if computer  == "Rock":
        print("you lose...!", computer, "smashes", player)
    else:
        print("you win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spellings!")