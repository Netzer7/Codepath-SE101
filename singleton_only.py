# Write the function `singleton_elements()` which takes a list and returns the elements that occur exactly once.

def singleton_elements(mylist):
  d = {}
  for num in mylist:
    if num in d:
      d[num] += 1
    else:
      d[num] = 1
  result = []
  for item, count in d.items():
    if count == 1:
      result.append(item)
  return result
# Test Cases
mylist = [1, 2, 1, 3, 3, 1]
print("Input: ", mylist)
print("Output: ", singleton_elements(mylist)) # [2]

mylist = [1, 2, 2, 6, 1, 3, 2]
print("\nInput: ", mylist)
print("Output: ", singleton_elements(mylist)) # [6, 3]

mylist = [2, 2]
print("\nInput: ", mylist)
print("Output: ", singleton_elements(mylist)) # []
