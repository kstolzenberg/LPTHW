# OOP process:  write or draw the problem, extract and research concepts, create a class hierarcht and object map, code classes.
# make a list of nouns and verbs in problem and write out how they are related
# then write down skeleton code - just classes and functions and nothing more and run it. build up incrementally
# simple game engine: "Gothons from Planet Percal #25"
# what is similar to what? this is a top-down approach
# start with a list of nouns and verbs and gradually expand to be objects!
# pass is a placeholder while you are working on code! it is ignored!

# review this game!!!!

# import exit function
from sys import exit
# import random interger function
from random import randint

class Scene(object):
    # basic object that all other scene objects inherit ... ie behavior you want all of the scenes to have!!!
    def enter(self):
        print "this scene is not yet configured. subclass it and impletment enter()"
        exit(1)

class Engine(object):
    # the engine is the actual game mechanism - creates it, plays it
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # function to loop through the different scenes
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        # this game works because each room has an enter method!
        current_scene.enter() 


# death is-a scene? inherits? yes
class Death(Scene):

    # list of quip strings
    quips = [
    "you died. you kinda suck at this.",
    "your mom would be proud. not.",
    "such loser.",
    "small dog is better than you at this."
    ]

    def enter(self):
        # select random phrase from quips list / adjust for zero index
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

# CC is-a scene
# the game structure is calling objects that contain functions with raw input and conditionals
class CentralCorridor(Scene):
    def enter(self):
        print "you are in space and you are being attacked what do you do?"
        action = raw_input("> ")

        # conditional to test input and then pick branches
        if action == "shoot!" :
            print "you are dead. then he eats you"
            return "death"
        elif action == "dodge!":
            print "whatever nice try and he eats ur head"
            return "laser_weapon_armory"
        else:
            print "DOES NOT COMPUTE"
            return "central_corridor"

class LaserWeaponArmory(Scene):
    def enter(self):    
        print "there is a bomba. guess the code"
        # set randoms for code
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        # test for user input against generated code
        while guess != code and guesses < 10:
            print "no."
            guesses += 1
            guess = raw_input("[keypad]> ")

        # create branch with if statement based on guess result compared to original value.
        if guess == code:
            print "put bbomb on the bridge"
            return "the_bridge"
        else:
            print "you fukced up. you die."
            return "death" 


class TheBridge(Scene):
    def enter(self):
        # test raw_input against options
        print "what do you do wif da bomb?"
        action = raw_input("> ")
        if action == "throw the bomba":
            print "it goes off"
            return 'death'
        elif action == "careful bomb":
            print "get thee to the escape pod"
            return "escape_pod"
        else:
            print "donest compute"
            return "the_bridge"

class EscapePod(Scene):
    # raw_input and branch with if statements
    def enter(self):
        print "you are at the pods. which do you take?"
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "you fukced up"
            return "death"
        else:
            print "you won!"
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "woweee you won"
        return "finished"
        

# this inherits from 'object' and is the contemporary way to do things. without is the older version
class Map(object):
    # this object holds all the scenes
    # a dictionary with string keys and functions for each scene
    scenes = {
    "central_corridor" : CentralCorridor(),
    "laser_weapon_armory" : LaserWeaponArmory(),
    "the_bridge" : TheBridge(),
    'escape_pod' : EscapePod(),
    'death' : Death(),
    'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

# actually call the objects and create instances
# a_map is-a new Map instance and the start scene is set to central corridor
a_map = Map('central_corridor')

# a_game is-a new Engine instance that passes a_map
a_game = Engine(a_map)

# Engine method - play on instance
a_game.play()





