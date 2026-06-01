student_profile = ("Aarav", "Grade 6", "Section A", 6)
print("Student Profile:", student_profile)
st_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
tot_sub = student_profile[3]
print("Student Name:", st_name)
print("Grade:", grade)
print("Section:", section)
print("Total Subjects:", tot_sub)
print("First two details:", student_profile[0:2])
mon_sub = {"Math", "Science", "English", "Computer", "Art"}
tue_sub = {"Math", "History", "English", "Sports", "Music"}
print("Monday Subjects:", mon_sub)
print("Tuesday Subjects:", tue_sub)
mon_sub.add("Library")
print("add :", mon_sub)
mon_sub.discard("Art")
print("discard:", mon_sub)
all_subjects = print(mon_sub.union(tue_sub))
common_subjects = print(mon_sub.intersection(tue_sub))
only_monday = print(mon_sub.difference(tue_sub))
only_tuesday = print(tue_sub.difference(mon_sub))
different_subjects = print(mon_sub.symmetric_difference(tue_sub))






