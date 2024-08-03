# Write a program to detect double space in a string.

# string = "i am  boy"

# index = string.find("  ")
# print(index)

string = "I am a  boy"
index = string.find("  ")

if index == -1:
    print("false")
else:
    print("true")



