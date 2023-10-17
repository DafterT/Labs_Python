# Простой цикл с enumerate
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_ = 0
index_of_none = -1
for i, j in enumerate(numbers):
    if j is None:
        index_of_none = i
    else:
        sum_ += j
average = sum_ / len(numbers)
numbers[index_of_none] = average
print("Измененный список:", numbers)

# Простой цикл с enumerate
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_ = 0
index_of_none = -1
len_of_numbers = len(numbers)
for i in range(len_of_numbers):
    number_with_index_i = numbers[i]
    if number_with_index_i is None:
        index_of_none = i
    else:
        sum_ += number_with_index_i
average = sum_ / len_of_numbers
numbers[index_of_none] = average
print("Измененный список:", numbers)
