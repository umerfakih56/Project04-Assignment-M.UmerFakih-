# Mad libs Python Project
# In this Kylie Ying tutorial, you will learn how to get input from the user, work with f-strings, and see your results printed to the console.

# This is a great starter project to get comfortable doing string concatenation in Python.

def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks below:")
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    
    story = f"Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb}. " \
            f"Every day, the {noun} would go on an adventure and make new friends."
    
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
