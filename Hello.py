# This program says hello and asks for my name

print ('Hello world')
print ('What is your name?') # Ask for their name
myName = input()
print ('it is good to meet you, ' + myName)
print ('The length of your name is:')
print (len(myName)) 
print ('What is your age?') # Asks for their age
myAge = input() 
print ('you will be ' + str(int(myAge) + 1) + ' in a year.')
input("Press enter to close program")


