# This module contains functions for filtering student data.
from data_processing import display_students

def filter_students_by_major(student_list, major):
	"""
	Return a filtered list of students by major using a list comprehension.
	The function should:
	- Check if a student's major matches the given major (case insensitive).
	- Return a new list containing only students that match.
	"""
	filtered = [student for student in student_list if major.lower() == student.lower()]
	if student_list:
		print(f"\nMajors matching {major}:")
		display_students(filtered)
	else:
		print(f"\nThere are no results matching {major}.")