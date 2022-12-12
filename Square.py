# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]


l=list(map(int,input().split())) 
l1=list(map(lambda i:i**2,l))
print("Square the elements of the list:")
print(l1)


# def square(i):
#  return i**2
# l=[4, 5, 2, 9]
# l1=list(map(square,l))
# print("Square the elements of the list:")
# print(l1)