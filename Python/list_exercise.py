# Given a list [1,2,3,4], print out all the values in the list.
list = [1,2,3,4]

for val in list:
    print(val)

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

for val in list:
    print(val * 20)
# Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).

names = ["Elie", "Tim", "Matt"]

print([
        word[0]
        for word in names
    ])
# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
list.append(5)
list.append(6)


print([
        numbers
        for numbers in list
        if numbers % 2 == 0
    ])
# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
list1 = [1,2,3,4]
list2 = [3,4,5,6]
print([
        numbers1
        for numbers1 in list1
        for numbers2 in list2
        if(numbers1 == numbers2) 
    ])

print([
        numbers
        for numbers in list1
        if numbers in list2
    ])
# Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).
print([
        word[::-1].lower()
        for word in names
    ])

# Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).
string1 = "first"
string2 = "third"

print([
        word
        for word in string1
        if word in string2
    ])
# For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print([
        num
        for num in range(1,101)
        if num % 12 == 0
    ])
# Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
print([
        char
        for char in "amazing"
        if char not in ['a','e','i','o','u']
    ])
# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

print([[[0,1,2]] * 3])
# Generate a list with the value:

print([[
        num
        for num in range(10)
    ]] * 10)

# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]