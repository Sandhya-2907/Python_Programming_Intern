#Objective: To identify and fix errors in a Python program that validates user input.

def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18:
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. Age must be a numeric value and you must be at least 18 years old.")
        return None  # Add this line to explicitly return None for invalid input

if __name__ == "__main__":
    main()
