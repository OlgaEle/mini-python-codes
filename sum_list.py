numbers = [3, 4, 1, 2]

# 1st method
total = 0

for num in numbers:
    total += num

print(f"Sum of the list is: {total}")

# 2nd method using the built-in sum() function
def sum_list(numbers):
    return sum(numbers)

print("Sum of the list is: ", sum_list(numbers))

# 3rd method using a lambda function
sum_lambda = lambda nums: sum(nums) # lambda function to sum the list
print("Sum of the list using lambda: ", sum_lambda(numbers))

# 4th method using a list comprehension
def sum_list_comprehension(numbers):
    return sum([num for num in numbers])

print("Sum of the list using list comprehension: ", sum_list_comprehension(numbers))
