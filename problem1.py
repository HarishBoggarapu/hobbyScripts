# find the number of rotatiions of an array
# given a circulary sorted array of integers
# assuce no duplicates and rotation is anti-clockwise
import math


def nRotations(arr):
    # pivot property (min value in array) -> previous and next element are always greater
    low = 0
    high = len(arr) - 1
    guess = 0
    print('intial low: {}'.format(low))
    print('intial high: {}'.format(high))
    print('intial guess: {}'.format(guess))
    while(arr[low] > arr[high]):
        guess = math.ceil((low + high) / 2)
        if(arr[guess] >= arr[high]):
            low = guess
        else:
            high = guess
        print('guess: {}'.format(guess))
        print('low: {}'.format(low))
        print('high: {}'.format(high))
    print(low)


arr = [5, 6, 1, 2, 4]
print(arr)
nRotations(arr)
print(1 > 1)
