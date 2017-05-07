def difference(a,b):
	return a-b

print(difference(2,2) == 0)
print(difference(0,2) == -2)

def product(a,b):
	return a*b

print(product(2,2) == 4)
print(product(0,2) == 0)

def print_day(num):
	if num == 1:
		return "Sunday"
	elif num == 2:
		return "Monday"
	elif num == 3:
		return "Tuesday"
	elif num == 4:
		return "Wednesday"
	elif num == 5:
		return "Friday"
	elif num == 6:
		return "Saturday"
	elif num == 7:
		return "Sunday"
	else:
		return None

print(print_day(4) == "Wednesday")
print(print_day(41) == None)

def last_element(lst):
	if lst:
		return lst.pop()
	else: 
		return None

print(last_element([1,2,3,4]) == 4)
print(last_element([]) == None)

def number_compare(a,b):
	if a == b: 
		return "Numbers are equal"
	elif a > b:
		return "First is greater"
	else:
		return "Second is greater"

print(number_compare(1,1) =="Numbers are equal")
print(number_compare(2,1) == "First is greater")
print(number_compare(1,2) =="Second is greater")

def single_letter_count(str, char):
	return str.lower().count(char.lower())

print(single_letter_count('amazing','A') == 2)

def multiple_letter_count(string):
	dict1 = {}
	for var in string:
		if dict1.get(var):
			dict1[var] += 1
		else: 
			dict1[var] = 1
	return dict1

print(multiple_letter_count("hello")) # {h:1, e: 1, l: 2, o:1})
print(multiple_letter_count("person")) # {p:1, e: 1, r: 1, s:1, o:1, n:1})

def list_manipulation(arr, command1, command2, *num):
	if(command1 == "add"):
		if(command2 == "beginning"):
			arr.insert(0,num[0])
			return arr
		else:
			arr.extend([num[0]])
			return arr
	else: 
		if(command2 == "beginning"):
			return arr.pop(0)
		else:
			return arr.pop()

print(list_manipulation([1,2,3], "remove", "end") == 3)
print(list_manipulation([1,2,3], "remove", "beginning") == 1)
print(list_manipulation([1,2,3], "add", "beginning", 20)) # [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) # [1,2,3,30]

def is_palindrome(string):
	for index, var in enumerate(string):
		if var != string[len(string)-index-1]:
			return False
	return True
print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah') )# True
print(is_palindrome('robert') )# False

def frequency(arr, key):
	return arr.count(key)

print(frequency([1,2,3,4,4,4], 4) == 3)
print(frequency([True, False, True, True], False) == 1)

def flip_case(string, key):
	if not string: return ''
	if string[0] == key.lower():
		return string[0].upper() + flip_case(string[1:], key)
	elif string[0] == key.upper():
		return string[0].lower() + flip_case(string[1:], key)
	else:
		return string[0] + flip_case(string[1:], key)

print(flip_case("Hardy har har", "h")) # "hardy Har Har"

def multiply_even_numbers(lst):
	if not lst: return 1
	if lst[0] % 2 == 0:
		return lst[0] * multiply_even_numbers(lst[1:])
	else: 
		return multiply_even_numbers(lst[1:])

print(multiply_even_numbers([2,3,4,5,6]) == 48)

def mode(lst):
	max_number = 0
	max_freq = 0
	for num in lst:
		if lst.count(num) > max_freq:
			max_freq = lst.count(num)
			max_number = num
	return max_number

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) == 4)

def capitalize(string):
	return string.capitalize()

print(capitalize("tim") == "Tim")
print(capitalize("matt") == "Matt")

def compact(lst):
	newlst = []
	for element in lst:
		if element:
			newlst.append(element)

	return newlst


print(compact([0,1,2,"",[], False, {}, None, "All done"]))# [1,2, "All done"]

def is_even(num):
    return num % 2 == 0

def partition(lst, fn):
	newlst = [[],[]]
	for val in lst:
		if fn(val):
			newlst[0].append(val)
		else:
			newlst[1].append(val)
	return newlst


print(partition([1,2,3,4], is_even))

def intersection(lst1, lst2):
	newlst = []
	for var1 in lst1:
		for var2 in lst2:
			if var1 == var2:
				newlst.append(var1)
	return newlst

print(intersection([1,2,3], [2,3,4]))

def add(a,b):
    return a+b

def once(fn):
	def inner(a,b):
		if inner.counter == 0:
			inner.counter += 1
			return fn(a,b)
		else: 
			return None
	inner.counter = 0
	return inner

one_addition = once(add)

print(one_addition(2,2)) # 4
print(one_addition(2,2)) # undefined
print(one_addition(12,200)) # undefined

def run_once(old_function):
	def new_function(a,b):
		if new_function.counter == 0:
			new_function.counter += 1
			return old_function(a,b)
		else:
			return None
	new_function.counter = 0
	return new_function

@run_once
def add(a,b):
    return a+b

print(add(2,2)) # 4
print(add(2,20)) # None
print(add(12,20)) # None





