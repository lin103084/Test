import random

# 這是一個隨機生成的 Python 程式碼

def generate_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(20)]
    return numbers

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum

def find_max(numbers):
    max_num = max(numbers)
    return max_num

random_numbers = generate_random_numbers()
print("隨機生成的數字:", random_numbers)

odd_numbers = filter_odd_numbers(random_numbers)
print("奇數:", odd_numbers)

sum_result = calculate_sum(random_numbers)
print("總和:", sum_result)

max_number = find_max(random_numbers)
print("最大數:", max_number)
