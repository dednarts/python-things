#card object array of objects 
#needs to have name value and number 
import random
from cardmodule import Card
from hand import Hand
import time


def draw_card(deck,given_hand):                 #this function recursively searches for a new card if the value is true, ive never been able to properly apply and understand recursion until now and im so happy
    random_number = random.randrange(0,52)      #dance dance dance

    if deck[random_number].inhand != True:
        given_hand.cards_in_hand.append(deck[random_number])
        deck[random_number].inhand = True
        return given_hand
    else:
        return draw_card(deck,given_hand)
    
def print_both_scores(dealer,player):
    print(f"Your Score was {player.total_score}")
    print(f"Dealer's Score was {dealer.total_score}")

def start_game(dealer,player,deck): #this function will be used for resetting and starting the game
    player.clear_hand() #here we are cleaning the pallette for both hands
    dealer.clear_hand()

    for cards in range(0,52):
        game_deck[cards].inhand = None 
    
    draw_card(game_deck,dealer)   #drawing cards
    draw_card(game_deck,dealer)  
    dealer.get_score() 
    print("The dealer has drawn 2 cards.\n")
    time.sleep(1)

    print("The player will now draw 2 cards\n")
    draw_card(game_deck,player)   
    draw_card(game_deck,player) 
    print("The Dealer will now draw 2 cards and the player will be given 2 cards.")



if __name__ == '__main__':
    game_deck = []
    dealer = Hand(True) #dealer condition applied to the dealer hand
    player = Hand()
    player_input = ''
    game_reset = ''
    game_win = None

    for create_func in range(0,52):               #here we initialize the deck of cards
        game_deck.append(Card(create_func))

    for cards in range(0,52):                                           #inside the for loop we are creating the cards in the deck
        game_deck[cards].name = game_deck[cards].determine_card()       #giving the card its name
        game_deck[cards].value = game_deck[cards].create_value()        #giving the card its value (except for aces)

    print("Welcome to Python Blackjack\nThe game will now begin.\nIt's time to shuffle the deck, it will be shuffled 3 times.")
    shuffle_statement = "Shuffling deck."       #wanted to use time cus bored boring bore

    for times in range(0,3):
        random.shuffle(game_deck)
        print(shuffle_statement)
        time.sleep(1)
        shuffle_statement = shuffle_statement + '.'

    start_game(dealer,player,game_deck)


    while True:
        print("Your hand is: ")
        player.print_hand(player.cards_in_hand)
        player_input = str(input(f"\nYour score is {player.get_score()}, hit or stand > "))
        player_input = player_input.lower()
        while True:

            if player_input == 'hit' or player_input == 'stand' :
                break
            else:        
                player_input = str(input("\nInvalid input, please enter hit or stand. > "))
                player_input = player_input.lower()
        

        if player_input.startswith('hit'):            
            draw_card(game_deck,player) 
            player.get_score()
            if player.total_score > 21:
                player.print_hand(player.cards_in_hand)
                print_both_scores(dealer,player)
                print("Player score has gone over 21, you lose!")
                game_win = True
                
        elif player_input.startswith('stand'): #player will compare cards with the dealer to see if they won or not based on score
            if player.total_score > dealer.total_score:
                print_both_scores(dealer,player)
                print("Player score has beaten the dealer, you win!")
                game_win = True
                
            elif player.total_score == dealer.total_score:
                print_both_scores(dealer,player)
                print("Player score matches dealer score, sorry house wins! (you lose)")
                game_win = True
                
            elif dealer.total_score > 21:
                print_both_scores(dealer,player)
                print("Dealer scored over 21, player wins!")
                game_win = True
               
            elif dealer.total_score > player.total_score:
                print_both_scores(dealer,player)
                print("Dealer scored higher than player, house wins!")
                game_win = True
              

        if game_win == True:
            game_reset = str(input("\nWould you like to play again? Please enter Y or N to continue? > "))
            game_reset = game_reset.upper()

            while True:
                if game_reset == 'Y':
                    player.clear_hand()
                    dealer.clear_hand()
                    start_game(dealer,player,game_deck)
                    game_win = None
                    break
                elif game_reset == 'N':
                    #close game and ty message
                    print("Thank you for play Blackjack with us!")
                    exit()
                else:
                    game_reset = str(input("Error: Invalid input. Please enter Y or N to continue? > "))
                    game_reset = game_reset.upper()
                    



        
    
    





    '''
    to do list
    finish game
    make gaem
    add erorr checks
    add win conditions
    possibly  create a separate file for the functions?
    become the incarnate of death
    jooba jooba hoop
    add user input for the ace card - have like a check_ace function or something like that
    avoid vidooe ghames 

    '''