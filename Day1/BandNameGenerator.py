"""
This is the project for the first day which was exceptionally easy since I 
have background in python programming, though it had been a long time since I coded in python.
"""


print("Welcome to the Band Name Generator!")
cityName = str(input("What is the name of the city you grew up in? "))
print(cityName)
petName = str(input("What is your pet's name? "))
print(petName)
bandName = cityName + " " + petName
print(f"Your band name could be {bandName}.")