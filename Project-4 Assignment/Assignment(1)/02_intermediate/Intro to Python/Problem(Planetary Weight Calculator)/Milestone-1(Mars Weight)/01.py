
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

# x = 3.1415926
# rounded_x = round(x, 2) # rounds x to 2 decimal places 
# print(rounded_x) 

# # This would print out out 3.14

# x = 2.71828
# rounded_x = round(x, 4)
# print(rounded_x)

# # This would print out 2.7183

# x = 3
# rounded_x = round(x, 4)
# print(rounded_x) 

# # This would print 3
# # Note that the round function does not add on decimal places that are not there already 

# Sample Run

# $ python marsweight.py

# Enter a weight on Earth: 120

# The equivalent on Mars: 45.36 

# Sample Run

# $ python marsweight.py

# Enter a weight on Earth: 186

# The equivalent on Mars: 70.31


def mars_weight():
    print("Welcome to the Mars Weight Calculator!")
    print("-----------------------------------")
    
    try:
        earth_weight = float(input("Enter your weight on Earth (in kg): "))
        if earth_weight <= 0:
            print("Weight must be a positive number. Please try again.")
            return
        
        mars_weight = round(earth_weight * 0.378, 2)
        print(f"Your weight on Mars would be: {mars_weight} kg")
        
        print("-----------------------------------")
        print("Fun Fact: Due to Mars' lower gravity, you could jump about 2.5 times higher than on Earth!")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    mars_weight()
