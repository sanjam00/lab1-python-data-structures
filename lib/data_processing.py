# This module contains functions to process student data.
from student_data import students

def format_student_data(student):
	"""
	Format student data for display.
	The function should return a formatted string containing:
	- Student ID
	- Student Name
	- Major
	such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
	"""

	print(f"Student ID: {student[0]} | Student Name: {student[1]} | Major: {student[2]}")


def display_students(student_list):
	"""
	Display all student records.
	Loop through the student_list and print each student using format_student_data().
	"""
	# i accomplished the objective with just display_students. 
	# idk how i'm supposed to implement format_student_data, seems like unnessary code.
	# nvm i figured it out :D

	for student in student_list:
		format_student_data(student)
		# print(f"Student ID: {student[0]} | Student Name: {student[1]} | Major: {student[2]}")
		

# format_student_data(students)
display_students(students)