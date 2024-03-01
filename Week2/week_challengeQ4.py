# Accept user input to create the first set of integers
input_str1 = input("Enter integers separated by spaces for the first set: ")
set1 = set(map(int, input_str1.split()))

# Accept user input to create the second set of integers
input_str2 = input("Enter integers separated by spaces for the second set: ")
set2 = set(map(int, input_str2.split()))

# Create a new set that contains only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Print the common elements to the console
print("Common elements in both sets:", common_elements)
