def find_min(*numbers):
    min_val = numbers[0]

    for number in numbers:
        if number < min_val:
            min_val = number

    return min_val

print(find_min(5, 2, 9, 1, 7))
print(find_min(3))
print(find_min(-5, 0, 5))