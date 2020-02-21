class Hand():

    def __init__(self,dealer_condition = None):
        self.total_score = 0
        self.cards_in_hand = []
        self.dealer_condition = dealer_condition #dealer condition for the sake of setting the aces by default 

    def get_score(self): #this is the function that uses the cards in hand list and iss going to calculate the total_score integer
        self.total_score = 0 #here we reset the score variable and as we iterate through the list we add the total amount of cards 
        for card_object in self.cards_in_hand:  
            if card_object.name.startswith('Ace') and card_object.value == 0:
                while True: #error check for the card value
                        if self.dealer_condition == True:
                            card_object.value = 11
                            break
                        
                        try:
                            card_object.value = int(input("Ace card. Please enter either 1 or 11 as the card's value > "))
                        except ValueError:
                            print("Error: Please enter a number (1 or 11) as the card's value > ")
                            continue
                        else:
                            if card_object.value == 1 or card_object.value == 11:
                                break  
        
            self.total_score += card_object.value

        #print(f"{self.total_score}")
        return self.total_score

    def print_hand(self, cards_in_hand): #prints hand self explanatory
        for cards in cards_in_hand:
            print(cards.name)
        pass

    def clear_hand(self): #removes all cards from the hand
        for cards in self.cards_in_hand:
            self.cards_in_hand.remove(cards)

