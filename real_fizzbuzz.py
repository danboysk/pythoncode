#!/usr/bin/python3
import unittest

class Solution:
  def fizzBuzz(self, n: int) -> list[str]:
    result = []
    # ADD CODE HERE!
    # count = 0
    # while (count < n):
    for count in range (1, n + 1):
       count = count + 1
       # print ("current count: ", count)
       if (count % 3 == 0) and (count % 5 != 0):
           result.append("Fizz")
       elif (count % 3 != 0) and (count % 5 == 0):
           result.append("Buzz")
       elif (count % 3 == 0) and (count % 5 == 0):
           result.append("FizzBuzz")
       else: 
           result.append(str(n))
       # print ("Result contains: ", result)
    return result


class FizzBuzzTest(unittest.TestCase):
  def test_fizzbuzz_basic(self):
      """Tests basic functionality with multiple inputs."""
      solution = Solution()

      self.assertEqual(solution.fizzBuzz(15), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])

if __name__ == "__main__":
  unittest.main()

