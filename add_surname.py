# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/03/2024

# Define a function named add_surname that takes as a parameter a list of first names

def add_surname(names):
    # Use of list comprehension to filer names that start with "K" and "Kardashian"
    return [name + "Kardashian" for name in names if name.startswith ("K")]
