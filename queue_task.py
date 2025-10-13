import random
from queue import Queue
import time

class Server:
    def __init__(self):
        self.players = 0
        self.max_players = 5
        self.queue = Queue()

    def connect_player(self):
        if self.players >= self.max_players:
            print("Server is full!")
            return
        if not self.queue.is_empty():
            self.players += 1
            player_name = self.queue.dequeue()
            print(f"Player {player_name} connected")

    def disconnect_player(self):
        if self.players == 0:
            return
        print("Player disconnected")
        self.players -= 1
        self.connect_player()

    def add_player(self, player_name):
        self.queue.enqueue(player_name)
        self.connect_player()

server = Server()

while True:
    if random.randint(0, 1):
        server.disconnect_player()
    else:
        server.add_player(f"Player_{random.randint(1, 100)}")
    print(f"Server online: {server.players}")
    print("Server queue:")
    server.queue.display()
    time.sleep(1)