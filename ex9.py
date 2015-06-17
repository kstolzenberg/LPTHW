# 2 ways to make code across different lines
# """/""" and \n

days = "Mon Tue Wed Thu Fri Sat Sun"
# what is n? and the backsplash?
# '\n' seemed to be new line? no "n" = string
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# maybe these are lists that we can pass after strings?
print "Here are the days: " , days
print "Here are the months: " , months

# this is a multiline comment no? no! this was a multiline string.
print """
there is something going on here.
with the three double-quotes.
we'll be able to type as much as we like.
even 4 lines if we want or 5 or 6.
"""