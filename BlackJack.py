
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs") 
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
values = {"Ace":1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven":7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}




                                                                   # ======= CARD CLASS ======

class Card:

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit 
		self.value = values[rank]

	def __str__(self):                                
		return f"{self.rank} of {self.suit}"

	def card_name(self):
		return f"{self.rank} of {self.suit}"



		                                                             # ======= DECK CLASS ======


class Deck:

	def __init__(self):
		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				created_card = Card(rank,suit)
				self.all_cards.append(created_card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def remove_one(self):
		return self.all_cards.pop()



                                                                   # ====== GAMER CLASS ======


class Gamer:                                     

	def __init__(self, balance = 100):
		self.balance = balance 
		self.name = input("What's your name? ")
		print(f"Welcome {self.name}! You have {self.balance}$ to play with. Have fun!")
		self.gamer_cards = []

        
	def hits(self,new_card):
		self.gamer_cards.append(new_card)
		return self.gamer_cards

    
	def ace_choice(self):
		if card.rank == "Ace":
			ace_value = int(input("You have drawn an Ace. Choose its value to continue: 1 or 11 "))
		else:
			ace_value = 0
		return ace_value


    
	def gamer_sum(self, ace_val):
		gamer_score = 0
		for card in self.gamer_cards:
			if card.rank == "Ace":
				gamer_score += ace_val
			else:
				gamer_score += card.value
		return gamer_score


	def places_bet(self):
		bet = " "
		while bet.isdigit() == False:
			bet = input("How much do you want to bet? ")  
			if bet.isdigit() == False:
				print("You have to type in a number!!")
			else:
				int_bet = int(bet)
				if self.balance > int_bet:
					self.balance -= int_bet
					print(f"You have bet {int_bet}$. You have {self.balance}$ left. You can now draw cards from the deck.")
				else:
					while self.balance <= int_bet:
						print(f"{self.name}, you don't have enough money you addicted gambler go home \nJust kidding make a new bet.")
						int_bet = int(input("Make smaller offer: ")) 
					self.balance -= int_bet
					print(f"You have bet {int_bet}$. You have {self.balance}$ left. You can now draw cards from the deck.")
		return int(bet)
                    
                    
	def gets_money(self, bet):
		self.balance += bet                                    
		print(f"{self.name}'s balance: {self.balance}")




                                                               # ====== DEALER CLASS ======
class Dealer:

	def __init__(self, balance = 0):
		self.dealer_cards = []
		self.balance = balance

	def hits(self,new_card):
		self.dealer_cards.append(new_card)
		return self.dealer_cards

	def dealer_sum(self):
		dealer_score = 0
		for card in self.dealer_cards:
			dealer_score += card.value           #Ace value is going to be 1 by default
		return dealer_score
    
	def gets_money(self, bet):
		self.balance += bet                                    
		print(f"Dealer's balance: {self.balance}")




                                                              # ====== GAME LOGIC ======
def replay():
    
    return input('Wanna try again? Enter Yes or No: ').lower().startswith('y')

print("Welcome to BlackJack!")

comp = Dealer()
player = Gamer()

while True:
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        new_deck = Deck()                 
        new_deck.shuffle()
        player.gamer_cards = []
        comp.dealer_cards =[]

    # player: set up cards and calculate score
        print("Here are your cards: ")
        for i in range(0,2):
            card = new_deck.remove_one()
            player.hits(card)
        for card in player.gamer_cards:
            print(card)
        ace_value = player.ace_choice()
        score = player.gamer_sum(ace_value)
        print(f"Your total is {score}")

    # player sees dealer's card
        new_card = new_deck.remove_one()
        print(f"Dealer's card is: {new_card.card_name()}")
        comp.hits(new_card)
        dealer_score = comp.dealer_sum()

    # player places bet 
        bet = player.places_bet()

    # player hits until they want to stop
        keep_hitting = input("Do you want to draw a card? Yes or No? ")
        while score < 21:
            while keep_hitting.lower()[0] == "y":
                card = new_deck.remove_one()
                player.hits(card)
                print(f"You have drawn: {card.card_name()}")
                if card.rank == "Ace":
                    ace_val = player.ace_choice()
                    score = player.gamer_sum(ace_val)
                else:
                    score = player.gamer_sum(ace_value)
                print(f"Your new total is {score}")
                if score >=21:
                    break
                else:
                    keep_hitting = input("Do you want to draw a card? Yes or No? ")
            if keep_hitting.lower()[0] == "n":
                while dealer_score <= score:
                    new_card = new_deck.remove_one()
                    print(f"Dealer has drawn: {new_card.card_name()}")
                    comp.hits(new_card)
                    dealer_score = comp.dealer_sum()
                    print(f"Dealer's sum is: {dealer_score}")
                if dealer_score == 21 or (dealer_score > score and dealer_score < 21):
                    print("Dealer wins!")      
                    comp.gets_money(bet)
                    print("Game over")
                    game_on = False
                    break
                elif dealer_score >21:
                    print(f"Dealer busted! {player.name} wins!")
                    player.gets_money(bet)
                    print("Game over")
                    game_on = False
                    break
        if score == 21:
            print(f"{player.name} wins!")
            player.gets_money(bet)
            print("Game over")
            game_on = False
        elif score >21:
            print(f"{player.name} has busted... dealer wins")
            comp.gets_money(bet)
            print("Game over")
            game_on = False

    if not replay():
        break

print("Hello World")