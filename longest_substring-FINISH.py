def longest_substring(s):
  currentMax = 1:
  
  ptr1 = 0
  ptr2 = 1
  while ptr2 <= len(s):
    currentLength = 0
    if s[ptr1] != s[ptr2]:
      currentLength += 1
    if currentLength > currentMax:
      currentMax = currentLength
    ptr1 += 1
    ptr2 +=1
  return currentMax

# Test Cases
s = "pppppp"
print("Input: ", s)
print("Output: ", longest_substring(s)) # 1

s = "aabdcefabcbb"
print("\nInput: ", s)
print("Output: ", longest_substring(s)) # 6