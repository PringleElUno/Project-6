# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/03/2024

# Define a class named Person that has two private data members - the person's name and age

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    # Get the age to return it
    def get_age(self):
        return self._age
def std_dev (person_list):
    if len(person_list) == 0:
        return None

    #Calculate the average age
    total_age = sum ([person.get_age() for person in person_list])
    mean_age = total_age / len(person_list)

    #Calculate the sum of squared differences from the mean value
    sum_squared_diff = sum([(person.get_age() - mean_age) ** 2 for person in person_list])

    #Calculating the standard deviation
    std_dev_result = (sum_squared_diff / len(person_list)) ** 0.5
    #Return that standard deviation to find the result
    return std_dev_result
