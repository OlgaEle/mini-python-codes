# 🔍 1st method using modulus (%) operator
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 🔍 2nd method using bitwise AND operator (&)
number = int(input("Enter a number:"))

if number & 1: # this uses the least significant bit (LSB) to determine odd/even
    # If the least significant bit is 1, the number is odd
    # If the least significant bit is 0, the number is even
    # For example, 5 in binary is 101, and the LSB is 1, so it's odd
    # I find this method exciting :)
    print(f"{number} is odd")
else:
    print(f"{number} is even")

# 🔍 3rd method using functions (reusable code)
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def check_number(n):
    if is_even(n):
        return f"{n} is even"
    elif is_odd(n):
        return f"{n} is odd"
    
number = int(input("Enter a number: "))
print(check_number(number))

# 🔍 4th method using a lambda function
check_even_odd = lambda n: f"{n} is even" if n % 2 == 0 else f"{n} is odd" # is good for quick checks
number = int(input("Enter "))
print(check_even_odd(number))

# 🔍 5th method using a list comprehension
def check_even_odd_list(numbers): # this method is useful for checking multiple numbers at once
    return [f"{n} is even" if n %2 == 0 else f"{n} is odd" for n in numbers]

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()] # the .split() method splits the input string into a list of strings (based on spaces by default)
print(check_even_odd_list(numbers))

# 🔍 6th method using a map function
def check_even_odd_map(numbers):
    return list(map(lambda n: f"{n} is even" if n % 2 == 0 else f"{n} is odd", numbers)) # map applies the lambda function to each element in the numbers list
numbers = [int(x) for x in input ("Enter numbers separated by space: ").split()]
print(check_even_odd_map(numbers))

# 🔍 7th method using a filter function
def filter_even(numbers):
    return list(filter(lambda n: n % 2 == 0, numbers)) #filter returns only the even numbers from the list

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(filter_even(numbers))

# ⌛️ Compare methods by time taken
import time

def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.8f} seconds")

def main():
    number = int(input("Enter a number: "))
    
    print("\nUsing modulus operator:")
    time_function(lambda n: f"{n} is even" if n % 2 == 0 else f"{n} is odd", number)
    
    print("\nUsing bitwise AND operator:")
    time_function(lambda n: f"{n} is odd" if n & 1 else f"{n} is even", number)
    
    print("\nUsing functions:")
    time_function(check_number, number)
    
    print("\nUsing lambda function:")
    time_function(check_even_odd, number)
    
    numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
    
    print("\nUsing list comprehension:")
    time_function(check_even_odd_list, numbers)
    
    print("\nUsing map function:")
    time_function(check_even_odd_map, numbers)
    
    print("\nUsing filter function:")
    time_function(filter_even, numbers)

if __name__ == "__main__":
    main() 
    stop = input("Press Enter to exit...")
