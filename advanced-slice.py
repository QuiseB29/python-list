temperature = [72, 75, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperature = temperature [7:14]
print ("Temperature for the second week", second_week_temperature) #Extract temperatures for the second week

above_temperature = temperature [25:30] #Extract temperatures above 100
print("Temperature above 100")
print(above_temperature)

temperature.reverse()
reverse_temperature = temperature [5:10]
print("Temperature on the 5th and 10th day")
print(reverse_temperature)