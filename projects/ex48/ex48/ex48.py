# making advanced user imput - accept plain english and understand

# go through a list of words and figure out their type using a tuple = list that you can't change (x,y,c)
#second_word = ('direction', 'north')

# you can stash lists as values in a dict!!! you can't have multiple keys per value in a dict
lexicon = {
    'direction':['north', 'south','east','west', 'down', 'up', 'left', 'right', 'back'],
    'verbs':['go', 'stop', 'kill', 'eat'],
    'stop words':['the', 'in', 'of','from','at','it'],
    'nouns':['door', 'bear', 'princess', 'cabinet'],
    'numbers':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
}

def scanner(user_input):
    #return a sentence that is composed of a list of tuples with (TOKEN, WORD parings)
    words = user_input.split(' ') # this splits a string into a list

    print words
    print lexicon.values()

    # need to reach down deeper into the dict

    for item in words:
        for tuples in lexicon.iteritems():
            if item in lexicon.values():
                print "hi"
            else:
                print "nope"

        #word_type = (TYPE, WORD) #lexicon['']

        #sentence = []
        #sentence.append(word_type)
        #return sentence



stuff = raw_input('> ')
scanner(stuff)





