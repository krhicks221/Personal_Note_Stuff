#Python bs I guess

a = 5
b = a
output = 5

b += 13
b
output = 5

a
output = 5

losers = ("Brett", "Jack", "Logan")
winners = losers
winners
output = ("^")

winners.append("Lynzie") #.append adds a specified thing () to the end of the list
winners = ["Brett", "Jack", "Logan"]
losers = winners
losers
output = ["^"]

winners.pop(0) #.pop takes a value out of the list and returns it () specifies which part of the list should be removed
output = "Brett"

winners
output = ["Jack", "Logan"]

losers
output = ["Jack", "Logan"]

#list only stored once
#losers and winners pointing at the same thing
