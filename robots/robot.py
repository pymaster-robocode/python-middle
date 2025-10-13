class Robot:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.__health = health
        self.__damage = damage
        self.__energy = 100

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, min(value, 200))

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        if value >= 0:
            self.__damage = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__energy = max(0, min(value, 100))

    def attack(self, other):
        if self.energy < 10:
            print(f"{self.name} has no energy!")
            return
        print(f"{self.name} attacks {other.name} for {self.damage} dmg.")
        self.energy -= 10
        other.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} got {amount} dmg. HP: {self.health}")
        if self.health <= 0:
            print(f"{self.name} destroyed!")

    def is_alive(self):
        return self.health > 0

    def status(self):
        print(f"{self.name}: HP={self.health}, Energy={self.energy}")