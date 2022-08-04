import random

card_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_list=[]
computer_list=[]
player_total=0
computer_total=0
ace_count_player=0
ace_count_computer=0
player_flag=True


game_input=input("Do you want to play a game of Blackjack?Type 'yes' or 'no'")

def player_card():
        global player_total
        global ace_count_player
        new_card=random.choice(card_list)
        player_list.append(new_card)
        ace_count_player=player_list.count(11)
        if(player_total>21 and ace_count_player==1):
               player_total=player_total-10
        else:
               player_total=player_total+new_card

def computer_card():
    global computer_total
    global ace_count_computer
    computer_flag=True
    while computer_flag:
        if(computer_total>21 and ace_count_computer!=0):
                computer_total=computer_total-10
                
        if(computer_total<17):
            new_card=random.choice(card_list)
            computer_list.append(new_card)
            ace_count_computer=computer_list.count(11)
            computer_total=computer_total+new_card
        else:
            computer_total=computer_total
            computer_flag=False

def game_output():
       print(f"Your card {player_list}")
       print(f"Your current score:{player_total}")
       print(f"Computer first card:{computer_list}")

if(game_input=="yes"):
# player and computer getting first 2 cards and their total
    for i in range(0,2):
        player_list.append(random.choice(card_list))
        ace_count_player=player_list.count(11)
        player_total=player_total+player_list[i]
        computer_list.append(random.choice(card_list))
        ace_count_computer=computer_list.count(11)
        computer_total=computer_total+computer_list[i]
    game_output()

else:
    print("Thank you")

while player_flag:
    player_input=input("Type 'yes' to get another card, type 'no' to pass ")
    if(player_input=="yes"):
        player_card()
        game_output()
    elif(player_input=="no"):
        player_flag=False
        computer_card()

print(f"Computer first card:{computer_list}")
print(f"Computer current score:{computer_total}")

if(computer_total==21):
    print("You lose")
elif(player_total==21):
    print("You win")
elif(player_total>21):
    print("You lose")
elif(computer_total>21):
    print("You win")
elif(player_total>computer_total):
    print("You win")
elif(player_total==computer_total):
    print("Draw")
else:
    print("You lose")

