# Write a program to fill in a letter template given below with name and date
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
afterreplace = letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050")
print(afterreplace)

