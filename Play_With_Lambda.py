# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35


x=int(input("Enter a number : "))
y = lambda x,y : x+y
print("Output :", y(x,25))


# x = lambda n : n + 25
# print("Output :", x(10))