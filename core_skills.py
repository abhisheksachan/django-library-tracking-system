import random

# Create a list of 10 random numbers between 1 and 20.

random_numbers = [random.randint(1, 20) for i in range(10)]
print(f"random_numbers: {random_numbers}")

# Filter Numbers Below 10 (List Comprehension)
filtered_random_numbers = [num for num in random_numbers if num < 10]
print(f"filtered_random_numbers: {filtered_random_numbers}")

# Filter Numbers Below 10 (Using filter)
filter_random_numbers = list(filter(lambda x: x < 10, random_numbers))
print(f"filter_random_numbers: {filter_random_numbers}")

