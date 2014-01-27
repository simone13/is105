#-- coding: utf-8 --
cars = 100 #antall biler
space_in_a_car = 4.0 #plass til antall personer i bil
drivers = 30 #antall sjåfører
passengers = 90 #antall passasjerer
cars_not_driven = cars - drivers #antall biler som ikke brukes = biler - sjåfører
cars_driven = drivers #biler som brukes = antall sjåfører
carpool_capacity = cars_driven * space_in_a_car #biler som deles = Biler som kjøres * plass i bil
average_passengers_per_car = passengers / cars_driven #gjennomstittelig passasjerer per bil = passasjerer / antall biler som blir brukt


print "There are", cars, "cars available." #Viser antall biler
print "There are only", drivers, "drivers available."#viser antall sjåfører
print "There will be", cars_not_driven, "empty cars today." #viser antall ubrukte biler
print "We can transport", carpool_capacity, "people today." #viser hvor mange personer som kan fraktes
print "We have", passengers, "to carpool today." #viser antall passasjerer
print "We need to put about", average_passengers_per_car, "in each car." #viser gjennnomsnittelig antall passasjerer i hver bil
