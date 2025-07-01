# Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

print("\tSelection letter")
letter = '''Dear <|Name|>,
    You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Vatsal").replace("<|Date|>", "4 june 2025"))