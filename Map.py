# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]


l=[1, 2, 3, 4, 5, 6, 7]
l1=list(map(lambda i:i*3,l))
print("Triple of list numbers:")
print(l1)


# def triple(i):
#  return i*3
# l=[1, 2, 3, 4, 5, 6, 7]
# l1=list(map(triple,l))
# print("Triple of list numbers:")
# print(l1)