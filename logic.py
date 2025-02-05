import random
rock=('''
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_|''')

print(rock)
paper=(''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     ''')
print(paper)
scissors=('''  ,--.
 (    )____ ___________________________
  `--'---,-'  ,.  T--------------------`-.
  ,--.---`-.  `'  |_dd____________________`>
 (    )"""" """""""""""""""""""""""""""""""
  `--' ''')
print(scissors)
print (" ")

user_choice=int(input("what do you choose ? type 0 for Rock , 1 for Paper , 2 for Scissors "))
print("you have choosen :  ",user_choice)
computer_choice=random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice==computer_choice:
    print("it is a tie ")
elif user_choice ==0 and computer_choice ==1 :
    print("you lose")
elif user_choice ==0 and computer_choice ==2 :
    print("you win")
elif user_choice ==1 and computer_choice ==0 :
    print("you win")
elif user_choice ==1 and computer_choice ==2 :
    print("you lose")
elif user_choice ==2 and computer_choice ==0 :
    print("you lose")
else :
    print("you win")

    # R BEATS S
    # S BEATS P
    # P Beats R

#r p s
#0 1 2