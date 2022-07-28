def most_common_letters(letter_counts):
  currentMax = 0;
  maxChar = []
  for count in letter_counts.values():
    if count > currentMax:
      currentMax = count;
  for letter, count in letter_counts.items():
      if count == currentMax:
        maxChar.append(letter)
  return maxChar    

#Test Cases
letter_counts = {'c': 1, 'a': 3, 'r': 2, 't': 2, 'b': 1}
print("Input: ", letter_counts)
print("Output: ", most_common_letters(letter_counts)) # ['a']

letter_counts = {'c': 1, 'a': 3, 'r': 3, 't': 3, 'b': 1}
print("\nInput: ", letter_counts)
print("Output: ", most_common_letters(letter_counts)) # ['a', 'r', 't']
