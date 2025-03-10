numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_numbers = sum(numbers[0:4]+numbers[5:])
count_numbers = len(numbers)
avg_numbers = sum_numbers / count_numbers
numbers[4] = avg_numbers

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
