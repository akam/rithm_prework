def add_student(first_name):
	with open('students.txt', 'a+') as file:
			if not file.tell():
				file.write('Name')
			file.write('\n' + first_name)
			print(file.read())

def find_student(first_name):
	with open('students.txt', 'r') as file:
			if first_name in file.read():
				return first_name
			else:
				return "not found"

def update_student(first_name, last_name):
	with open('students.txt', 'r+') as file:
		contents = file.read()
		contents = contents.replace(first_name, last_name)
		file.seek(0)
		file.write(contents)
		file.truncate()

def remove(first_name):
	with open('students.txt', 'r+') as file:
		contents = file.read()
		contents = contents.replace(first_name+ '\n', '')
		file.seek(0)
		file.write(contents)
		file.truncate()
