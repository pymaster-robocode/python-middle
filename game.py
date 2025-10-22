class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_game(self):
        p1_card = self.p1.draw()
        p2_card = self.p2.draw()
        if not p1_card or not p2_card:
            return self.p1_score, self.p2_score

        print(f"P1: {p1_card} VS P2: {p2_card}")
        card_won = self.fight(p1_card, p2_card)
        if card_won:
            if card_won == p1_card:
                self.p1_score += 1
            if card_won == p2_card:
                self.p2_score += 1
            print(f"Winner: {card_won}")
        else:
            print("Draw!")
        print(f"Scores: P1: {self.p1_score} - P2: {self.p2_score}")

        self.play_game()
        return None

    @staticmethod
    def fight(card1, card2):
        res_1 = card1.attack - card2.defense
        res_2 = card2.attack - card1.defense
        if res_1 > res_2:
            return card1
        elif res_1 < res_2:
            return card2
        else:
            return 0