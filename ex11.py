# exersise 11 : Asking questions

print "How old are you?", 
age = int(raw_input())  #casting raw_input"string" as int

#input will set the variable type to whatever type it looks like
#if it is a number it will set to int or double, raw_input always returns strings

height = raw_input("How tall are you? ") # shows a different way to prompt user

print "how much do you weigh?",
weight = input()  # using input

print "So, your're %d old, %r tall and %r heavy." % ( age, height, weight )