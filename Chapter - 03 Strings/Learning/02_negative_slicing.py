name = "Harry"
print(name[0:3]) # start from index 0 all the way till 3 (excluding 3)

print(name[-4:-1])
print(name[1:4])

print(name[:4]) # is same as print print(name[1:4])
print(name[1:]) # is same as print(name[1:5])

# skip slicing
a = "012345678901"
print(a[1:8:3])
print(a[1:11:3])
