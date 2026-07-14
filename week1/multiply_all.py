def multiply_all(*nums):
    result = 1

    for num in nums:
        result = result * num

    return result

print(multiply_all(2, 3, 4))
print(multiply_all(3, 2, 1))
print(multiply_all(1, 2, 3, 4, 5, 6,7))
