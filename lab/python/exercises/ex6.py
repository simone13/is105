#-- coding: utf-8 --
x = "There are %d types of people." % 10 #det er x antall personer
binary = "binary" #bineær
do_not = "don't" #ikke
y = "Those who know %s and those who %s." % (binary, do_not) #det er de som kan og de som ikke kan

print x #viser x
print y #viser y

print "I said: %r." % x #viser x igjen
print "I also said: '%s'." % y #viser y igjen

hilarious = False #statement, viser falskt
joke_evaluation = "Isn't that joke so funny?! %r" #statement

print joke_evaluation % hilarious #viser begge øvrige statements

w = "This is the left side of..." #dette er venstre side
e = "a string with a right side." #dette er høyresiden av en string

print w + e #viser w og e
