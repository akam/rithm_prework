import csv

with open('users.csv') as file:
	reader = csv.DictReader(file, delimiter = '|')
	rows = list(reader)
	for row in rows:
		print(row)

with open('users.csv', 'a') as file:
	full_name = input("Enter your full name: ")
	new = full_name.split(" ")
	data_writer = csv.writer(file, delimiter = '|')
	data_writer.writerow(new)
