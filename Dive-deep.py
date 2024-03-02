students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

student_info = [{"name": name, "grade": grade, "activity": activity} for name, grade, activity in zip (students, grades, activities)]
print("List of dictionary")
for info in student_info:
    print(info) #Combine list
    
    student_info_filterd =[{"name": name, "grade": grade, "activity": activity} for name, grade, activity in zip(students, grades, activities)]
    print("Grades not lower the 80")
    for info in student_info_filterd:
        print(info) #Filtered out students who grades under 80
         
grades_passed = [{"name": name, "grade": grade, "activity": activity} for name, grade , activity in zip (students, grades, activities) if grade >=80]
for info in grades_passed:
    info[''] = "Passed"
    print(info)
 
