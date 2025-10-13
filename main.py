import random
import time

from robots.defenderbot import DefenderBot
from robots.energybot import EnergyBot
from robots.robot import Robot


class BattleArena:
    def __init__(self, bots):
        self.bots = bots

    def start_battle(self):
        round_number = 1
        print("\nBattle start!\n")
        while self.count_alive() > 1:
            print(f"\nRound {round_number}")
            attacker, target = self.choose_two_alive()
            print(f"{attacker.name} VS {target.name}\n")
            attacker.attack(target)
            target.attack(attacker)
            self.print_status()
            if self.count_with_energy() <= 0:
                print("\nBattle end! No winner!\n")
                return
            round_number += 1
            time.sleep(1)

        winner = self.get_alive_bot()
        print(f"\nWinner: {winner.name}!")

    def count_alive(self):
        return len([b for b in self.bots if b.is_alive()])

    def count_with_energy(self):
        return len([b for b in self.bots if b.energy > 0 and b.health > 0])

    def choose_two_alive(self):
        alive = [b for b in self.bots if b.is_alive()]
        return random.sample(alive, 2)

    def get_alive_bot(self):
        for bot in self.bots:
            if bot.is_alive():
                return bot
        return None

    def print_status(self):
        print("\n")
        for bot in self.bots:
            bot.status()

if __name__ == "__main__":
    bots = [
        DefenderBot("DefenderBOT", health=120, damage=8),
        EnergyBot("EnergyBOT", health=10, damage=10),
        Robot("DefaultBOT")
    ]

    arena = BattleArena(bots)
    arena.start_battle()
