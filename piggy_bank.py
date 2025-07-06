# 1st method using a list (and functions)
piggy_bank = []

def add_money(amount):
    if amount > 0:
        piggy_bank.append(amount)
        print(f"Added ${amount} to the piggy bank.")
    else:
        print("Please enter a valid amount to add.")

def remove_money(amount):
    total = sum(piggy_bank)
    if amount > 0 and amount <= total:
        new_total = total - amount
        piggy_bank.clear()
        if new_total > 0:
            piggy_bank.append(new_total)
        print(f"Removed ${amount} from the piggy bank. New balance is ${new_total}.")
    else:
        print("Invalid amount to remove. Please enter a valid amount that is less than or equal to the current balance.")   

def check_balance():
    total = sum(piggy_bank)
    print(f"Total balance in the piggy bank: ${total}")

def main():
    while True:
        print("\n🐷 Piggy Bank Menu:")
        print("1. Add Money 💵")
        print("2. Remove Money 💸")
        print("3. Check Balance 🔎")
        print("4. Exit ❌")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            amount = float(input("Enter the amount to add: "))
            add_money(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to remove: "))
            remove_money(amount)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Exiting the Piggy Bank. Bye! 🤗")
            break

if __name__ == "__main__":
    main()

# 2nd method using class
class PiggyBank: # this defines a PiggyBank class. A class is like a blueprint for creating objects (for example, a piggy bank)
    def __init__(self): # __init__ is used to initialize the object when it is created. It sets up the initial state of the PiggyBank
        self.balance = 0 # self refers to the current object (here means the balance of this PiggyBank object)
    
    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount} to the Piggy Bank.")
        else:
            print("Please enter a valid amount to add.")
    
    def remove_money(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Removed ${amount} from the Piggy Bank. New balance is ${self.balance}.")
        else:
            print("Invalid amount to remove. Please enter a valid amount that is less than or equal to the current balance.")
    
    def check_balance(self):
        print(f"Total balance in the Piggy Bank: ${self.balance}")

def main():
    bank = PiggyBank() # bank is an object of the PiggyBank class
    while True:
        print("\n🐷 Piggy Bank Menu:")
        print("1. Add Money 💵")
        print("2. Remove Money 💸")
        print("3. Check Balance 🔎")
        print("4. Exit ❌")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            amount = float(input("Enter the amount to add: "))
            bank.add_money(amount) # is a method
        elif choice == '2':
            amount = float(input("Enter the amount to remove: "))
            bank.remove_money(amount) # is a method
        elif choice == '3':
            bank.check_balance() # is a method
        elif choice == '4':
            print("Exiting the Piggy Bank. Bye! 🤗")
            break

if __name__ == "__main__":
    main()

# Some notes:
# A class is a blueprint for creating objects. It defines the properties and behaviors that the objects will have.
# An object is something you create from a class. It's like a real-world item made from a blueprint.
# A method is a function that belongs to an object. It's like an action that the object can perform.

# So, in short:
# - A class is a blueprint (like a recipe).
# - An object is what you can build from that blueprint (like a cake made from the recipe).
# - An object can have properties (like the color or size of the cake).
# - A method is an action that an object can perform (like slicing the cake).

# Another note:
# When I was creating the PiggyBank class, I thought I should put the new total and clear() as I did in the first method, but I realized that it is not necessary. The balance is already updated in the class, so I just need to print the new balance.
# I mean that in the first method I used a list to store the balance, so I had to clear the list and append the new total.
# In the second method, I used a single variable (self.balance) to store the balance, so I didn't need to clear or recalculate anythinng because self.balance always holds the current balance.
# In short: with a list, I had to manage all the items and recalculate the total.
# With a class and a single variable, I just update the number.

# Pros of using a variable:
# - Simplicity: Easier to understand and manage.
# - Efficiency: Less overhead compared to managing a list.
# - Clarity: The balance is always clear and straightforward.
# - Less memory usage: No need to store multiple items, just one number.
