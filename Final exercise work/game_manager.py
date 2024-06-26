#File name: game_manager.py
#Author: Henry Våg
#Description: Interacts with the modules according to main.py

from inventory import Inventory
from game import Game, Digitalgame
from validator import *
from user import User

class GameManager:
    # Initializing GameManager
    def __init__(self, inv):
        self.inv = inv
        self.users = {}
        self.logged_user = ""
    
    def order(self):
        # Prompting user to order a game and updating inventory accordingly
        print("Which game would you like to order?")
        title = input("Title:")
        genre = input("Genre:")
        qty = input("How many copies?:")
        type = input("Which type? y = digital / n = disc:")
        self.users[self.logged_user].add_game(title, genre, qty, type)
        print(self.inv.subtract_game(title, qty, type))

    def list_games(self):
        # Listing all available games in the inventory
        self.inv.list_games()

    def add_new_game(self):
        # Creates new game object and passes it into the function which adds it to the inventory

        print("-----------")
        title = input("title:")
        if valid_title(title):
            genre = input("genre:")
            if valid_genre(genre):
                type = input("digital y/n?:")
                if valid_type(type):
                    qty = int(input("quantity:"))

                    if type == "y":
                        game = Digitalgame(title, genre, qty)
                    if type == "n":
                        game = Game(title, genre, qty)

                    self.inv.add_game(game)
    
    def create_user(self):
        # Creating a new user account
        name = input("enter name:")
        if not self.name_in_use(name):
            password = input("enter password:")         
            new_user = User(name, password) 
            if not self.users:
                new_key = 1
            else:
                new_key = max(self.users) + 1

            self.users[new_key] = new_user
            return True
        else:
            print("name already in use")
            return False
    
    def login(self):
        # Logging in existing user
        name = input("enter name:")
        password = input("enter password:")
        for user_key, user in self.users.items():
            if name == user.name and password == user.password:
                print("logged in")
                user.logged_in = True
                self.logged_user = user_key
                return True
        print("no matching username and password")
        return False
    
    def logout(self):
        # Logs out current user
        self.logged_user = ""
    
    def name_in_use(self, name):
        # Checks if username already in use
        for user_key, user in self.users.items():
            if name == user.name:
                return True
        return False
    
    def user_list_games(self):
        # Lists games owned by logged-in user
        user = self.users[self.logged_user]
        user.list_games()
            
gamemgr = GameManager(Inventory())
