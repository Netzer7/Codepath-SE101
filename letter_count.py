def letter_count(word_list):
  dictionary = {}
  for word in word_list:
    for char in word:
      if char in dictionary:
        dictionary[char] += 1
      else:
        dictionary[char] = 1
  return dictionary
# Test Cases
word_list = ['car', 'bat', 'rat']
print("Input: ", word_list)
print("Output: ", letter_count(word_list)) # {'c': 1, 'a': 3, 'r': 2, 'b': 1, 't': 2}

word_list = []
print("\nInput: ", word_list)
print("Output: ", letter_count(word_list)) # {}
