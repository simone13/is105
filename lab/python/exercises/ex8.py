#-- coding: utf-8 --
formatter = "%r %r %r %r" #forteller hvor mange ganger det skal printes

print formatter % (1, 2, 3, 4) # printer 1,2,3,4
print formatter % ("one", "two", "three", "four") #printer one,two,three,four
print formatter % (True, False, False, True) #printer true, false, flase, true
print formatter % (formatter, formatter, formatter, formatter) #viser hvor mange %r du får
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #printer statement i rekkefølge
