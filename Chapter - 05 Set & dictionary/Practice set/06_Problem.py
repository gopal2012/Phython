#  Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

d = {}
name = input("Enter Friends name: ")
leng = input("Enter Language name: ")

d.update({name: leng})
name = input("Enter Friends name: ")
leng = input("Enter Language name: ")

d.update({name: leng})
name = input("Enter Friends name: ")
leng = input("Enter Language name: ")

d.update({name: leng})
name = input("Enter Friends name: ")
leng = input("Enter Language name: ")

d.update({name: leng})

print(d)