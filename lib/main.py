from student_data import students
from filters import filter_students_by_major
from data_processing import display_students
from set_operations import unique_majors
from data_generator import student_generator

filtered_students = filter_students_by_major(students, "Mathematics")

# print(filtered_students)

# display_students(students)

display_students(filtered_students)

majors = unique_majors(students)
print(majors)

print("Student Major Generator")
for major_students in student_generator(students, "Physics"):
  print(major_students)