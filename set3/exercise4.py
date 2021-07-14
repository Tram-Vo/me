# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
from typing import Sequence

# import time


def binary_search(low, high, arr, x):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid -1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
    
    else: 
        return -1 

arr = [1, 5, 100]
x = 5

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("guess", str(result))
else:
    print("tries")



if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
