# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.


def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element modified successfully"
    return "Index out of range"

def slice_list(lst, start, end):
    return lst[start:end] if 0 <= start < len(lst) and 0 <= end <= len(lst) else "Invalid slice range"

def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(fruit_list, index))
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Result:", modify_element(fruit_list, index, new_value))
            print("Updated list:", fruit_list)
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(fruit_list, start, end))
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
