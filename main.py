import random
while True:
        number_of_players = input("Enter number of Players (Min 2 players | Max 4 players) : ")
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if int(number_of_players) > 4 or int(number_of_players)<2 :
                print ("Invalid Entry")
            else:
                 break;
        else:
            print("Enter a Valid Number")    

players_scores_tracker = [0 for i in range(int(number_of_players))]



def roll():
    dice = random.randint(1,6)
    return dice
i = 0
top_score = 50
while True:
   player_response = input(f"would you like to roll player {i+1} : (y/n) -").lower()
   if player_response == "y":
        current_roll_val = roll()
        print(f"You rolled a {current_roll_val}")
        if current_roll_val == 1:
             print("Your Roll value is 1 , You are OUT")
             players_scores_tracker[i] = 0
             i += 1
             if i >= number_of_players:
                  i=0
             continue;
        players_scores_tracker[i] += current_roll_val
        if players_scores_tracker[i] >= 50:
             print(f"Player {i+1} , You WON")
             break;
        print(f"Your current score is {players_scores_tracker[i]}")
   elif player_response == "n":
        i += 1
        if i >= number_of_players:
            i=0
            continue;
   else:
        print("Enter Y or N")











