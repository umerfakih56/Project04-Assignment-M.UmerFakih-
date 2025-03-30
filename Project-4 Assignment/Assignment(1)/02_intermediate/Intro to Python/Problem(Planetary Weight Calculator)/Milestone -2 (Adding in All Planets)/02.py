# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

# Sample Run

# $ python planetaryweight.py

# Enter a weight on Earth: 120

# Enter a planet: Mars

# The equivalent weight on Mars: 45.36

# Sample Run

# $ python planetaryweight.py

# Enter a weight on Earth: 150

# Enter a planet: Jupiter

# The equivalent weight on Jupiter: 354.0
# Useful Syntax

# Python has an if statement! This if statement passes if the value of x is the same as the value of y. x and y can be literal numbers, strings, variables, or constants.

# x = 42 y = 42

# if x == y: print("x and y are equal!")



def planetary_weight():
    print("Welcome to the Planetary Weight Calculator!")
    print("------------------------------------------")
    
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    try:
        earth_weight = float(input("Enter your weight on Earth (in kg): "))
        if earth_weight <= 0:
            print("Weight must be a positive number. Please try again.")
            return
        
        planet = input("Enter a planet: ")
        if planet not in gravity_factors:
            print("Invalid planet name. Please try again with a valid planet from the solar system.")
            return
        
        equivalent_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"Your weight on {planet} would be: {equivalent_weight} kg")
        
        print("------------------------------------------")
        print("Fun Fact: Gravity varies significantly across planets, affecting how you move and even how high you can jump!")
    except ValueError:
        print("Invalid input. Please enter a numerical value for weight.")

if __name__ == "__main__":
    planetary_weight()
