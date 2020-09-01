"""Program for a game of Blackjack."""

import random
from IPython.display import clear_output


class Card:
    """A class to represent each card in the deck, using two attributes, suit and rank."""
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
         
    def __str__(self):
        return self.rank + " of " + self.suit

    
class Deck:
    """A class to build out each card and store all 52 card objects which can later be shuffled."""
    
    def __init__(self): 
        self.deck_list = []

        for suit in suits:
            for rank in ranks:
                any_card = Card(suit, rank)
                self.deck_list.append(any_card)
                
    def shuffle(self):
        """A method to randomise the cards in the deck."""
        random.shuffle(self.deck_list)

    def deal(self):
        """A method to remove a single card from the deck list."""
        return self.deck_list.pop()      
    
    def __str__(self):
        print(len(self.deck_list))
        new = []
        for item in self.deck_list:
            new.append(str(item))
        return "\n".join(new)

    
class Hand:
    """A class to represent each player's hand and adjust the Ace value as neccessary."""
    
    def __init__(self):
        self.card_list = []
        self.sum = 0
        self.aces = 0
           
    def add_card(self, card):
        """A method that adds the dealt card to the hand and adds its value to the hand total."""
        self.card_list.append(card)
        self.sum += card.value
        
    def adjust_for_ace(self):
        """A method that adjusts the ace value to 1 if the hand total remains less than 21."""
        self.sum = 0
        for card in self.card_list:
            self.sum += card.value
        
        if self.card_list[-1].rank == "Ace":
            self.aces += 1
        if self.sum > 21:
            self.sum -= self.aces*10 
            
    def __str__(self):
        new_list = []
        for card in self.card_list:
            new_list.append(str(card))
        return "\n".join(new_list)

    
class Chips:
    """A class to keep track of a player's starting chips, bets and ongoing winnings."""

    def __init__(self, total = 100):
        self.total = total                                                                                                              
    def win_bet(self, bet):
        """A method adding the bet amount to the player's chips in a win-game scenario."""
        self.total += bet

    def lose_bet(self, bet):
        """A method subtracting the bet amount from the player's chips in a lose-game scenario."""
        self.total -= bet

    def __str__(self):
        return f"You have {self.total} chip(s)."

    
def welcome():
    """Function that prints out a welcome message to the game."""
    
    print("Welcome to Blackjack!\n")

    
def take_bet():
    """Function that asks the player how much they would like to bet."""
    
    global bet
    while True:
        try:
            bet = int(input("How much would you like to bet? "))
        except:
            print("Invalid bet! Please try again.")
        else:
            break

            
def hit(deck, hand):
    """Function that adds a new card to the dealers hand and adjusts the value of Aces."""
    
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()

    
def hit_or_stand(deck, hand):
    """Function that asks the player if they would like to hit or stand."""
    
    global playing
    acceptable_values = ["YES", "NO"]
    while True:
        answer = input("Would you like to hit? (Yes or No) ").upper()
        
        if answer not in acceptable_values:
            print("Invalid input! Enter 'Yes' or 'No'.")
        elif answer == "YES":
            clear_output()
            return True
            break
        else:
            clear_output()
            playing = False
            break

            
def show_some(player, dealer):
    """Function that reveals each of the players hands, keeping one dealer card hidden."""
    
    new_list = []    
    for card in dealer.card_list:
        new_list.append(str(card))
    new_list.pop(0)
    "\n".join(new_list)
    print(f"\nThe dealer has: \n{new_list[0]}\n")
    
    print(f"You have: \n{player}")
    print(f"\nYour hand total is: {player.sum}")

    
def show_all(player, dealer):
    """Function that reveals each of the player's hands."""
    
    print(f"Here are the dealer's cards: \n{dealer}\n")
    print(f"Dealer hand total: {dealer.sum}\n")
    
    print(f"Here is what you had: \n{player}\n")
    print(f"Player hand total: {player.sum}")

    
def replay():
    """Function that asks the player if they would like to continue playing."""
    
    ask = True
    acceptable_values = ["yes", "no"]
    while ask:
        choice = input("Would you like to continue? (Yes or No) ").lower()
        
        if choice not in acceptable_values:
            clear_output()
            print("Type 'Yes' or 'No'.")
        else:
            break
            
    if choice == "yes":
        clear_output()
        return True
    else:
        clear_output()
        print("\nThank you for playing!")
        return False

    
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
game_on = True
dealer_turn = True

player_chips = Chips()

welcome()
while game_on:
    new_deck = Deck()
    new_deck.shuffle()

    dealer = Hand()
    hit(new_deck, dealer)
    hit(new_deck, dealer)

    player = Hand()
    hit(new_deck, player)
    hit(new_deck, player)

    while True:
        print(player_chips)
        take_bet()
        if 0 < bet <= player_chips.total:
            clear_output()
            print(f"You bet: {bet}\nRemaining chips: {player_chips.total-bet}")
            break
        else:
            clear_output()
            print(f"You can only bet between 0 and {player_chips.total}.")

    show_some(player, dealer) 

    while playing: 
        if hit_or_stand(new_deck, player):
            hit(new_deck, player)
            clear_output() 
            show_some(player, dealer)
            
        if player.sum > 21:
            clear_output()
            print(f"\nPlayer went bust! The dealer wins!\n")
            player_chips.lose_bet(bet)
            playing = False
            dealer_turn = False

        elif player.sum == 21:
            clear_output()
            print(f"\nCongratulations! Player wins the game!\n")
            player_chips.win_bet(bet)
            playing = False    
            dealer_turn = False
            
    if dealer_turn == True:

        while dealer.sum < 17:
            hit(new_deck, dealer)

        if dealer.sum > 21:
            player_chips.win_bet(bet)
            print("\nThe dealer went bust! Player wins the game!\n")

        elif dealer.sum == 21:
            player_chips.lose_bet(bet)
            print("\nThe dealer scored 21 and won!\n")

        elif dealer.sum > player.sum and dealer.sum < 21:
            player_chips.lose_bet(bet)
            print("\nThe dealer won!\n")

        elif dealer.sum < player.sum and dealer.sum < 21:
            player_chips.win_bet(bet)
            print("\nThe dealer lost!\n")

        elif dealer.sum == player.sum:
            print("\nTie game! The amount you bet has been returned to your chips total.\n")

        elif dealer.sum > 21 and player.sum > 21:
            print("\nTie game! The amount you bet has been returned to your chips total.\n")
            
    show_all(player, dealer)
        
    if player_chips.total > 0:
        print(f"\nYou have {player_chips.total} chip(s) remaining.") 
        if replay():
            dealer_turn = True
            playing = True
            continue        
        else:
            game_on = False

    else:
        print("\nYou have no more chips remaining!")
        if replay():
            dealer_turn = True
            playing = True
            player_chips = Chips()
            continue
        else:
            game_on = False
            
