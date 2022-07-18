def similiar_string(string,list):
  similiar_index = 0;
  current_count = 0
  for index, word in enumerate(list):
    counter = 0;
    for char in word:
      if char in string:
        counter += 1
    if counter > current_count:
      current_count = counter
      similiar_index = index
  return list[similiar_index]

print(similiar_string("tangerine", ["tangle", "charge", "ring"]))
print(similiar_string("skyscraper", ["scrap", "sky", "pleasure"]))