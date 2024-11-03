# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/03/2024

#Define a function named find_median that takes as a parameter a list of numbers

def find_median(numbers):
    #sort the list of numbers
    numbers.sort()

    #The length of the list
    n = len(numbers)

    # Check if the number of elements are even or odd
    if n % 2 == 0:
        # If even, calculate the average of the middle number two
        mid1 = n // 2
        mid2 = mid1 - 1
        median = numbers[mid1] + numbers[mid2] / 2

    else:
        #if odd, simply take the middle value
        mid = n // 2
        median = numbers[mid]

    return median
