import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values =values[rank]
    def __str__(self):
        return self.rank +  " of " + self.suit

# two_of_hearts = card("Heart", "Value")

class Deck:
    def __init__(self):
        self.deck_cards =[]
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck_cards.append(created_card)
    def shuffle_deck(self):
        self.rand = random
        self.rand.shuffle(self.deck_cards)
    def deal_one(self):
        return self.deck_cards.pop()
class Player:
    def __init__(self, name):
        self.name = name
        self. deck_cards = []
    def remove_one(self):
        return self.deck_cards.pop(0)

    def add_card(self, new_card):
        if type(new_card) == type([]):
            self.deck_cards.extend(new_card)
        else:
            self.deck_cards.append(new_card)
    def __str__(self):
        return f"player {self.name} has {len(self.deck_cards)} cards"





# new_player = Player("Calvin")
# new_player.add_card([mycard, mycard, mycard])
# new_player.remove_one()
#
# print(new_player)
player_1 = Player("Calvin")
player_2 = Player("Shadeed")
new_deck = Deck()
new_deck.shuffle_deck()

for things in range(26):
    player_1.add_card(new_deck.deal_one())
    player_2.add_card(new_deck.deal_one())
game_on = True
round_num = 0
while game_on:
    round_num +=1
    print(f"Round {round_num}")
    if len(player_1.deck_cards) ==0:
        print("Calvin, out of cards! Shadeed wins!")
        game_on = False
        break
    if len(player_2.deck_cards)==0:
        print('Shadeed, out of cards! Calvin wins!')
        game_on = False
        break
player_1_cards =[]
player_1_cards.append(player_1.remove_one())
player_2_cards = []
player_2_cards.append((player_2.remove_one()))
at_war = True
while at_war:
    if player_1_cards[-1].value > player_2_cards[-1].value:
        player_1.add_card(player_1_cards)
        player_1.add_card(player_2_cards)

        at_war = False
    elif player_1_cards[-1].value < player_2_cards[-1].value:
        player_2.add_card(player_1_cards)
        player_2.add_card(player_2_cards)

        at_war = False
    else:
        print("War!")

        if len(player_1.deck_cards) <5:
            print("Calvin unable to declare war!")
            print("Shadeed wins!")
            game_on = False
            break
        elif len(player_2.deck_cards) <5:
            print("Shadeed unable to declare war!")
            print("Calvin wins!")
            game_on = False
            break
        else:
            for num in range(5):
                player_1_cards.append(player_1.remove_one())
                player_2_cards.append(player_2.remove_one())