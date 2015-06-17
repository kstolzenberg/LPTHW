# more about input, prompts and passing and combining inputs
# mixing terminal input and user input!

from sys import argv

script, user_name, job = argv
prompt = "so...? "

print "Hi %s, I'm the %s script and I work for the %s" % (user_name, script, job)
print "I'd like to ask you a few questions." 
print "do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
%s is going to want to hear this.
alright, so you said %s about liking me.
you live in %s. not sure where that is.
and you have a %s computer. nice!
""" % (job, likes, lives, computer)
# order matters! the order of the parameter = order that variables are passed
# very clean...keeps variables separate so you can modify without hunting!

