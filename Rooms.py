#!\Users\ccboy\Python\DarkRoom-I-master\Rooms.py
from sys import exit
from random import randint
import data

def death():
    print("YOU LOSE!")
    print(ways[int(randint(0,4))])
    exit(0)
class MainRoom(object):
    def begin():
        print("""Now you are in the MainRoom.
                 You can [go] to the next room or [sleep].
                 Input 'go' or 'sleep' to choose.
              """)
        answer = input(">")
        if answer == "go":
            print("PASS")
            BearRoom.begin()
        elif answer == "sleep":
            death()
class BearRoom(MainRoom):
    def begin():
        print("""Now a bear is in the middle of the room.
                 It walks to you slowly.\tSuddenly, it runs to you.
                 You can [catch] it or [run] away.
              """)
        answer = input(">")
        if answer == "catch":
            print("PASS")
            BearRoom.next()
        elif answer == "run":
            death()
    def next():
        print("""You kill the bear.\tGood!
                 Now there are two doors. One is made with gold. One is made with wood.
                 Would you like to open the [gold] door or the [wood] door.\tBe careful!
              """)
        answer = input(">")
        if answer == "gold":
            death()
        elif answer == "wood":
            print("PASS")
