class Card:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} (Atk: {self.attack}, Def: {self.defense})"

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def draw(self):
        return self.deck.draw_card()