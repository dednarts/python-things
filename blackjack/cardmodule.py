import random

class Card():

    def __init__(self,index): #only variable we need from the main is the index 
        self.index = index
        self.name = ''
        self.inhand = None
        self.value = 0
        
    def determine_card(self): #we need the index of the list in order to set the name of the card
        self.index += 1 # we set this equal to one because 13 % 0 is 0 and there is no card value with 0 except for ace which needs to be inputted
        if self.index >= 1 and self.index <= 13:
            if self.index % 13 == 1:            #card number 1, ace
                self.name = "Ace of Clubs"  
            elif self.index % 13 == 11:         #11 == 10, Kings
                self.name = "King of Clubs" 
            elif self.index % 13 == 12:
                self.name = "Queen of Clubs"    #12 == 11, Queen
            elif self.index % 13 == 0:
                self.name = "Jack of Clubs"     #13 == 12, Jack
            else:
                self.name = str(self.index % 13) + " of Clubs"

        elif self.index >= 14 and self.index <= 26:
            if self.index % 13 == 1:
                self.name = "Ace of Diamonds" 
            elif self.index % 13 == 11:
                self.name = "King of Diamonds" 
            elif self.index % 13 == 12:
                self.name = "Queen of Diamonds" 
            elif self.index % 13 == 0:
                self.name = "Jack of Diamonds" 
            else:
                self.name = str(self.index % 13) + " of Diamonds"

        elif self.index >= 27 and self.index <= 39:
            if self.index % 13 == 1:
                self.name = "Ace of Hearts" 
            elif self.index % 13 == 11:
                self.name = "King of Hearts" 
            elif self.index % 13 == 12:
                self.name = "Queen of Hearts" 
            elif self.index % 13 == 0:
                self.name = "Jack of Hearts" 
            else:
                self.name = str(self.index % 13) + " of Hearts"

        elif self.index >= 40 and self.index <= 52:
            if self.index % 13 == 1:
                self.name = "Ace of Spades" 
            elif self.index % 13 == 11:
                self.name = "King of Spades" 
            elif self.index % 13 == 12:
                self.name = "Queen of Spades" 
            elif self.index % 13 == 0:
                self.name = "Jack of Spades" 
            else:
                self.name = str(self.index % 13) + " of Spades"

        return self.name

    def create_value(self): #here we are creating the value of the card through the index
        '''
        this function is based upon the game rules that KING QUEEN JACK AND 10 ARE ALL EQUAL TO 10
        '''
        self.index += 0
        if self.index % 13 == 0: #in this outcome end if the card is an ace   
            self.value = 10
            return self.value
        elif self.index % 13 == 1:  #this out come is for the ace and doesnt need to be changed until user input
            return self.value
        elif self.index % 13 >= 10:
            self.value = 10           
            return self.value
        else:
            self.value = self.index % 13 #if the card isn't an ace then we just set it to whatever mod 13 is     
            return self.value


    def __str__(self):
        return "Error: Object of Card type"

