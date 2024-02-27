#!/usr/bin/python3

def is_multiple(Frule, Brule, numb):
    ans = ""
 
    # This function checks if a factor (factr) is a divisor of a number.

    # Args:
    #     factr: The factor to be checked.
    #     number: The number to be divided.

    #   Returns:
    #     A string indicating "Fizz", "Buzz" or "FizzBuzz" if Frule or Brule are factors of number, 
    #     otherwise the number is returned.
 
    if (numb % Frule == 0) and (numb % Brule != 0):
        ans = "Fizz"
    elif (numb % Frule != 0) and (numb % Brule == 0):
         ans = "Buzz"   
    elif (numb % Frule == 0) and (numb % Brule == 0):
        ans = "FizzBuzz"
    else: 
        ans = str(numb)
 
    return ans

def get_integer_input():
  
  # Prompts the user for an integer input and handles non-integer/non-numeric input gracefully.
  # Returns:
  #   The entered integer value.

  while True:
    try:
      number = int(input("Enter an integer: "))
      return number
    except ValueError:
      print("Invalid input. Please enter an integer.")


print("Enter a number for Fizz Rule: ")
# Example usage
FizzRule = get_integer_input()
print("Fizz Rule (Factor):", FizzRule)

print("Enter a number for Buzz Rule: ")
# Example usage
BuzzRule = get_integer_input()
print("Buzz Rule (Factor):", BuzzRule)


print("Enter the starting number from which to start testing: ")
# Example usage
Startno = get_integer_input()
print("Starting from:", Startno)

print("Enter the number end testing: ")
# Example usage
Endno = get_integer_input()
print("Starting from:", Endno)

for x in range(Startno, Endno + 1):
  result = is_multiple(FizzRule, BuzzRule, x)
  print(result)  # Output: Multiple


