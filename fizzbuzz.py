#!/usr/bin/python3

def is_multiple(factr, numb):
    ans = ""
 
    # This function checks if a factor (factr) is a divisor of a number.

    # Args:
    #     factr: The factor to be checked.
    #     number: The number to be divided.

    #   Returns:
    #     A string indicating "Multiple" if factr is a factor of number, otherwise "Non-Multiple".
 
    remainder = numb % factr

    if remainder == 0:
        return "Multiple"
    else:
        return "Non-Multiple"


def get_integer_input():
  """
  # Prompts the user for an integer input and handles non-integer/non-numeric input gracefully.

  # Returns:
  #   The entered integer value.
  """
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


# Example usage
result = is_multiple(3, 12)
print(result)  # Output: Multiple

result = is_multiple(5, 12)
print(result)  # Output: Non-Multiple
