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
            print("\n\tPASS\n")
            BearRoom.begin()
        elif "sleep" in answer:
            death()
        else:
            death()
class BearRoom(MainRoom):
    def begin():
        print("""\nNow a bear is in the middle of the room.
It walks to you slowly.\tSuddenly, it runs to you.
You can catch it or run away.\n""")
        answer = input("Player:\n")
        if "catch" in answer:
            print("\n\tPASS\n")
            BearRoom.next()
        elif "run" in answer:
            death()
        else:
            death()
    def next():
        print("""\nYou kill the bear.\tGood!
Now there are two doors. One is made with gold. One is made with wood.
Would you like to open the [gold] door or the [wood] door.\tBe careful!\n""")
        answer = input("Player:\n")
        if "gold" in answer:
            death()
        elif "wood" in answer:
            print("\n\tPASS\n")
            DiningRoom.begin()
        else:
            death()
class DiningRoom(object):
    def begin():
        print("""\nNow you are in the DiningRoom.
You can choose one food to eat.\tBe careful! Some of them are deleterious!
FOODLIST:
[1]. mushroom
[2]. pizza
[3]. nothing
Enjoy it!""")
        answer = int(input("Player:\n"))
        if answer == 1:
            print("\n\tPASS\n")
            DiningRoom.next()
        elif answer == 2:
            death()
        elif answer == 3:
            print("\n\tPASS\n")
            DiningRoom.next_2()
        else:
            death()
    def next():
        print("""\nNow you find that you can see at night.
Use this ability well!\n
Suddenly, the lights are out, the darkness is over you.
You are afraid. A few moments later, you see a man stand in the darkness.
I'm the Thanos. Says the man. Give me the magic mushroom, or I'll ki-ki-ki-ki-Ahchoo you!
What? You say. You'll 'ki-ki-ki-ki-Ahchoo' me?
I'll kill you! The man says. Give me the mushroom!
Wait, if you kill me, no one can give you magic mushroom. You say.
I have to get rid of this fake Thanos! You think. But what can you do? run away? Looking for reinforcements? Or run up and beat him?""")
        answer =  input("Player:\n")
        if "run" in answer:
            death()
        elif "reinforcements" in answer:
            death()
        elif "beat" in answer:
            print("\n\tPASS\n")
        else:
            death()
