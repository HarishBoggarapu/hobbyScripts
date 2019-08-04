
def root(x, n):
    epsilon = 0.001
    if (x <= 1):
        lowerBound = 0
        upperBound = 1
    else:
        lowerBound = 1
        upperBound = x
    guess = (lowerBound + upperBound) / 2
    print('lowerBound: {}'.format(lowerBound))
    print('upperBound: {}'.format(upperBound))
    print('guess: {}'.format(guess))
    print('================================')
    # print(guess)
    while(abs((guess**n) - x) > epsilon):
        if((guess**n) > x):
            upperBound = guess
        else:
            lowerBound = guess
        guess = (lowerBound + upperBound) / 2
        print('lowerBound: {}'.format(lowerBound))
        print('upperBound: {}'.format(upperBound))
        print('guess: {}'.format(guess))

    print('final guess: {}'.format(guess))


x = 100
n = 8
root(x, n)
print('actual: {}'.format(x**(1 / n)))
