# making advanced user imput - accept plain english and understand
# need to create a list of allowed words = 'lexicon'

lexicon = [
    "north",
    "south",
    "east",
    "west",
    'down',
    'up',
    'left',
    'right',
    'back',
    'go',
    'stop'
    'kill'
    ]

# need a way to break up sentences = split by spaces
stuff = raw_input('> ')
words = stuff.split()

# go through a list of words and figure out their type using a tuple = list that you can't change (x,y,c)
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]


def scanner(user_input):
    #return a sentence that is composed of a list of tuples with (TOKEN, WORD parings)
    words = user_input.split(' ') # this splits a string into a list

    print words

    result = []
    for item in words:
        if item in lexicon.values():
            print "hi"
        else:
            print "nope"