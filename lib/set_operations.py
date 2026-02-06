# This module contains operations related to sets.

def unique_majors(student_list):
  """
  Return a set of unique student majors using set comprehension.
  Extract the major field from each student record.
  """
  if student_list:
    return {student[2] for student in student_list}
