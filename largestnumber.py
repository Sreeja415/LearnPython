numbers = [2, 5, 8, 9, 6]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("The largest number is:", largest)