# Writing to files

employee_file = open("example.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("example.txt", "a")  # --> adding some text in the end of the file
employee_file.write("\nToby - E")
employee_file.close()

employee_file = open("example.txt", "w")  # --> overriding the entire file
print(employee_file.write("New text"))
employee_file.close()

employee_file = open("example.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("example1.txt", "w")  # --> we're creating a new file as well
print(employee_file.write("New text fo run"))
employee_file.close()

employee_file = open("example1.txt", "r")
print(employee_file.read())
employee_file.close()