import random

number = random.randint(1, 100)
guess = ''

while number != guess:
    print('Please guess a number 1 - 100: ')
    guess = raw_input()
    try:
         int(guess)
    except ValueError:
        print ("That is not a number!")
    else:
        if  (int(guess)) > number:
            print ('Too high!')
        if (int(guess)) < number:
            print ('Too low!')
        if (int(guess)) == number:
            break
print ('You got it!')
print (number)





