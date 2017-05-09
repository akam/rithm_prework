def add_student(first_name):
	with open('students.txt', 'a+') as file:
			file.write('\n' + first_name)
			print(file.read())

def find_student(first_name):
	with open('students.txt', 'r') as file:
			if first_name in file.read():
				return first_name
			else:
				return "not found"