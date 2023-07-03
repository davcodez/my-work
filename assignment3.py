def find_highest_lowest(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    return highest, lowest


numbers = []
for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)


highest_number, lowest_number = find_highest_lowest(numbers)


print("Highest number:", highest_number)
print("Lowest number:", lowest_number)
#THE END