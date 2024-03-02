numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Make a list with even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers")
print(even_numbers)

greater_number = [num for num in numbers if num > 5] #Numbers greater then 5
print("numbers greater then 5")
print(greater_number)

if 7 in numbers:
    print("Seven is a orginal")
else:
    print("Seven is not a original")