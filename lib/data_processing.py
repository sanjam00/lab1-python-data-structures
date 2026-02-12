# This module contains functions to process student data.
def format_student_data(student):
	"""
	Format student data for display.
	The function should return a formatted string containing:
	- Student ID
	- Student Name
	- Major
	such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
	"""
	if student:
		return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
	else:
		print("Error: Student data could not be accessed.")


def display_students(student_list):
	"""
	Display all student records.
	Loop through the student_list and print each student using format_student_data().
	"""

	if student_list:
		for student in student_list:
			print(format_student_data(student))
			# print(f"Student ID: {student[0]} | Student Name: {student[1]} | Major: {student[2]}")
	else:
		print("Error: Student data could not be found.")
		