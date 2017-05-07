# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).

list = [("name", "Elie"), ("job", "Instructor")]

print({element[0]:element[1] for element in list})

# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

print({list1[i]:list2[i] for i,v in enumerate(list1)})

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

print({var:0 for var in "aeiou"})

# Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. You should return something like this (Hint - use chr(65) to get the first letter):

print({i+1:chr(var) for i,var in enumerate(range(65, 65+26))})