def distinct_substrings(s):
  ptr1 = 0
  ptr2 = 3
  counter = 0
  while ptr2 <= len(s):
    char_list = []
    for char in s[ptr1:ptr2]:
      if char not in char_list:
        char_list.append(char)
    if len(char_list) == 3:
        counter += 1
    ptr1 += 1
    ptr2 += 1
  return counter
# Test Cases
s = "aababcabc"
print("Input: ", s)
print("Output: ", distinct_substrings(s))

s = "xyzzaz"
print("\nInput: ", s)
print("Output: ", distinct_substrings(s))