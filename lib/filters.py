# This module contains functions for filtering student data.
from lib.data_processing import display_students

def filter_students_by_major(student_list, major):
	"""
	Return a filtered list of students by major using a list comprehension.
	The function should:
	- Check if a student's major matches the given major (case insensitive).
	- Return a new list containing only students that match.
	"""
	# filtered = [student for student in student_list if student[2].lower() == major.lower()]
	if student_list:
		print(f"\nMajors matching {major}:")
		# return display_students(filtered)
		return [student for student in student_list if student[2].lower() == major.lower()]
	else:
		print(f"\nThere are no results matching {major}.")