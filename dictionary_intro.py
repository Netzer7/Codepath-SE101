def total_inventory(inventory, inventory2, item):
  sum = 0
  sum += inventory[item]
  sum += inventory2[item]
  return sum

def translate(original, translation):
  translated = []
  for word in original:
    translated.append(translation.get(word))
  return translated

print(total_inventory({"bananas": 5, "apples": 3}, {"bananas": 2}, "bananas"))
print(translate(["hello", "world"], {"hello": "hola", "world": "mundo"}))