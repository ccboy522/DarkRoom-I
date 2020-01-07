#!\Users\ccboy\Python\DarkRoom-I-master\Rooms.py
from sys import exit
from random import randint

def death():
    ways = ["You have nothing to eat!",
            "Your joke is less funny than your father's!",
            "BOOOOOOOOOOOOOOOOOM",
            "You died because you are too poor.",
            "Your Mum kill you because you haven't do your homework yet."
            "You died of fear."
            "You died because you didn't do your homework."
            "You're dead. There's no reason"
            "Virus invasion!"
            "Reject a face-saving offer."
            "Get ready for your death!"]
    print("\nYOU LOSE!")
    print(ways[int(randint(0,10))])
    exit(0)
class MainRoom(object):
    def begin():
        print("Welcome to the DarkRoom-I!\nIt's dark all around you")
        print("You: Aaaah! Where am I? Wait, I maybe in the…")
        print("GAME START")
        print("""Now you are in the MainRoom.
You can [go] to the next room or [sleep].
Input 'go' or 'sleep' to choose.\n""")
        answer = input("Player:\n")
        if answer == "go":
            print("PASS")
            BearRoom.begin()
        elif answer == "sleep":
            death()
class BearRoom(MainRoom):
    def begin():
        print("""Now a bear is in the middle of the room.
It walks to you slowly.\tSuddenly, it runs to you.
You can [catch] it or [run] away.\n""")
        answer = input("Player:\n")
        if answer == "catch":
            print("PASS")
            BearRoom.next()
        elif answer == "run":
            death()
    def next():
        print("""You kill the bear.\tGood!
Now there are two doors. One is made with gold. One is made with wood.
Would you like to open the [gold] door or the [wood] door.\tBe careful!\n""")
        answer = input("Player:\n")
        if answer == "gold":
            death()
        elif answer == "wood":
            print("PASS")
