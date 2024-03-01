numbers = input("Enter a list of integers: ") # Space the inegers you enter
numbers = numbers.split()
numbers = [int(x) for x in numbers]
print("The list of integers is: ", numbers)

sum = 0
for i in numbers:
    sum = sum + i
print("The sum of the list of integers is: ", sum)