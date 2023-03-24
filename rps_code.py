import random

def get_choices():
        player_choice = input("Select a choice: rock, paper or scissors")
        options = ["rock","paper","scissors"]
        computer_choice = random.choice(options)
        choices = {"player" : player_choice , "computer" : computer_choice}
        return choices
    

def check_win(player, computer):
        print (f"you chose {player} ,computer chose {computer}")
        if player == computer :
                return print("it's a tie")
                
              
        elif player == "rock":  
                if computer == "sciccors" :
                        return print("Rock smashes sciccors! You win")

        elif:
                return print("Paper covers rock! You lose")                   

        
        else player == "paper"
                if computer == "rock":
                        return print("Paper covers rock! You lose") 
        
        if computer == "rock":  
                return print("Rock smashes sciccors! You win")
                        
        else:
                        return print("Sciccors cuts paper! You lose")                   

       
        
