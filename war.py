'''
War game: 

Rueles:
1. Deal 52 cards equaly to 2 players A and B
2. All players place a card and a higher card wins. Winner takes
    all cards from deck. 
3. Gameplay: 
    If A > B (A takes cards from deck)
    If A < B (B takes cards from deck)
    If A == B (Each player place one more card. loop until A or B has higher card. Then player takes all those cards.)

4. Game over:
    if palyer A or b don't have any cards to play he loose the game.
'''

import random

#Card deck: 2,3,4,5,6,7,8,9,10,11(J),12(Q),13(K),14(A) x 4


class Game:
    # Create a players and a deck as an empty lists.
    def __init__(self):
        self.deck = []
        self.player_A_hand = []
        self.player_B_hand = []

    # Define game cards four time each number and shuffle a cards.
    def deck(self):
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
        deck = [card for card in cards for _ in range(4)]
        random.shuffle(deck)
        return deck

    #Split deck in half ang move to player lists
    def split_deck(self):
        cards_to_player = len(self.deck) // 2
        self.player_A_hand = self.deck[:cards_to_player]
        self.player_B_hand = self.deck[cards_to_player:]

    




# 




