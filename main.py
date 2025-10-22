from random import randint, shuffle
from names import names
from cards import Player, Card, Deck
from game import Game

game_cards = []

def card_generator():
    for n in names:
        game_cards.append(Card(n, randint(1, 5), randint(1, 5)))
    shuffle(game_cards)

card_generator()

deck_1 = Deck()
deck_2 = Deck()

deck_1.cards = game_cards[:len(game_cards) // 2]
deck_2.cards = game_cards[len(game_cards) // 2:]

Player_1 = Player("Player1", deck_1)
Player_2 = Player("Player2", deck_2)

game = Game(Player_1, Player_2)
game.play_game()
