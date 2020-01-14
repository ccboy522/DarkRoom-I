#!\Users\ccboy\Python\DarkRoom-I-master\Rooms.py
from sys import exit
from random import randint
from data import printdata

def death():
    print("\nYOU LOSE!")
    printdata()
    exit(0)
class MainRoom(object):
    def begin():
        print("Welcome to the DarkRoom-I!\nIt's dark all around you")
        print("You: Aaaah! Where am I? Wait, I maybe in the…")
        print("GAME START")
        print("""Now you are in the MainRoom.
You can go to the next room or sleep.
Input 'go' or 'sleep' to choose.\n""")
        answer = input("Player:\n")
        if "go" in answer:
            print("PASS")
            BearRoom.begin()
        elif "sleep" in answer:
            death()
class BearRoom(MainRoom):
    def begin():
        print("""Now a bear is in the middle of the room.
It walks to you slowly.\tSuddenly, it runs to you.
You can catch it or run away.\n""")
        answer = input("Player:\n")
        if "catch" in answer:
            print("PASS")
            BearRoom.next()
        elif "run" in answer:
            death()
    def next():
        print("""You kill the bear.\tGood!
Now there are two doors. One is made with gold. One is made with wood.
Would you like to open the [gold] door or the [wood] door.\tBe careful!\n""")
        answer = input("Player:\n")
        if "gold" in answer:
            death()
        elif "wood" in answer:
            print("PASS")
            DiningRoom.begin()
class DiningRoom(object):
    def begin():
        print("""Now you are in the DiningRoom.
You can choose one food to eat.\tBe careful! Some of them are deleterious!
FOODLIST:
[1]. mushroom
[2]. pizza
[3]. nothing
Enjoy it!""")
        answer = int(input("Player:\n"))
        if answer = 1:
            print("PASS")
            DiningRoom.next()
        elif answer = 2:
            death()
        elif answer = 3:
            print("PASS")
            DiningRoom.next_2()
        def next():
            print("""Now you find that you can see at night.
Use this ability well!""")
