# Write a function `add_digits()` that takes in a number and adds all of its digits until the result has only one digit and returns it. 

def add_digits(num):
  currentSum = 0
  while num > 0:
    currentSum += num % 10
    num = num // 10
    if currentSum < 10 and num == 0:
      return currentSum
    elif currentSum >= 10 and num == 0:
      num = currentSum
      currentSum = 0
  return num
  
# Test Cases
num = 38
print("Input: ", num)
print("Output: ", add_digits(num)) # 2

num = 0
print("\nInput: ", num)
print("Output: ", add_digits(num)) # 0

num = 42
print("\nInput: ", num)
print("Output: ", add_digits(num)) # 6

num = 89
print("\nInput: ", num)
print("Output: ", add_digits(num)) # 8