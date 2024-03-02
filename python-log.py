grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93] #Sort grades in descending order 
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

sum = sum(grades)  # find the average of the grades
average = sum/len(grades)
print(average)

for i in range(len(grades)): #Replacing any grade under 80 with "Failed"
    if grades[i] < 80:
        grades[i] = "Failed"
        print(grades)
        
        grades.append ("Passed")
        print(grades)