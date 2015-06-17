# make a game where you run through rooms

from random import choice

class Room(object):
    def __init__(self):
        pass

class Kitchen(Room):
    def speech(self):
        print "so u landed at the kitchen."
        k_ask = raw_input("mr bear what snacks do you have? \n")

        if "drinks" in k_ask:
            print "welp you gotta pee"
            return "pee"
        elif "sandwiches" in k_ask:
            print "you gotta sleeeeep"
            return "sit"
        else:
            print "u done"
            return 

class Living(Room):
    def speech(self):
        print "so u found ur way to the living rm"
        l_ask = raw_input("what are you reading? \n")

        if "book" in l_ask:
            print "you must be hungry"
            return "cook"
        else:
            print "u done"
            return 

class Bath(Room):
    def speech(self):
        print "so u found ur way to the bath rm"
        b_ask = raw_input("what is your favorite bath? \n")

        if "bubbles" in b_ask:
            print "you gotta sleeeeep"
            return "sit"
        else:
            print "u done"
            return 

class Nav(object):
    # dict outside of function and the class has to be after the other ones!
    all_rooms = {
        "cook" : Kitchen(),
        "sit" : Living(),
        "pee" : Bath(),
        }

    def __init__(self):
       pass

    def walk(self, start_rm):
        # access the dict via a variable input
        current_rm = Nav.all_rooms.get(start_rm)
        # this will dump you to the speech method of whatever is queried from all_rooms!
        return current_rm.speech() 

    # this is a debug test!
    def printy(self, words):
        print words


# call the objects
house = Nav()
# how to make this keep going? this only goes 1-deep - this could be done wayyyy bettter!
#house.walk("cook")

# get random start from dict
random_start = choice(house.all_rooms.keys())

#call your walk function 3 times - how could you do this better?
house.walk(house.walk(house.walk(random_start)))












