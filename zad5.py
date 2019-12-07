from random import randint

def guessWhatNumber(min, max):
    success = False
    myNumber = randint(min,max)
    please = 'Please give me a number between {} and {}: \n'.format(min,max)
    while success == False:
        yourNumber = input(please)
        if isNumber(yourNumber) and isNumberBetween(int(yourNumber), min, max):
            if myNumber == int(yourNumber):
                success = True 
            else:
                print('Nope, try again \n')
        else:
            print('I am sorry Dave, I am afraid I cannot do that \n')

    print('You lucky bustard! It was {}!\n'.format(myNumber))

def isNumber(text):
    try:
        int(text)
        return True
    except:
        return False

def isNumberBetween(number, min, max):
    if number > max or number < min:
        return False
    else:
        return True

guessWhatNumber(1,9)