import random

red = 'yes'

print random.randint(1, 6)
while red != 'No':
    print('Do you want to roll again?: ')
    red = raw_input()
    print random.randint(1, 6)

print ("Good-bye!")




