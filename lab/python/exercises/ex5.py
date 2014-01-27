#-- coding: utf-8 --
my_name = 'Simon Eriksen' #navn
my_age = 21 #alder
my_height = 179 # cm
my_weight = 90 # kg
my_eyes = 'Green' #øyenfarge
my_teeth = 'White' #tannfarge
my_hair = 'Blonde' #hårfarge

print "Let's talk about %s." % my_name #viser navn
print "He's %d cm tall." % my_height #viser høyde
print "He's %d kg heavy." % my_weight #viser vekt
print "Actually that's not too heavy." #statement
print "He's got %s eyes and %s hair." % (my_eyes, my_hair) #viser øyenfarge og hårfarge
print "His teeth are usually %s depending on the coffee." % my_teeth #statement, inkluderer tannfarge


print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight) #adderer alder, høyde, vekt, alder, høyde og vekt
