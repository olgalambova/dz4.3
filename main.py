import random
numbers = []
numbers_len = random.randint(1, 10)
for _ in range(numbers_len):
    numbers.append(random.randint(1, 10))
print(numbers_len)
print(numbers)

result_numbers = [numbers[0], numbers[2], numbers[-2]]
print(result_numbers)
