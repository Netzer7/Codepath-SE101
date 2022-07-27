def same_name (dictionary):
  sameList = []
  for owner,dog in dictionary.items():
    if owner == dog:
      sameList.append(owner)
  return sameList
def dog_name_frequencies(dicitionary2):
  nameDict = {}
  for name in dicitionary2.values():
    if name in nameDict:
      nameDict[name] += 1
    else:
      nameDict[name] = 1
  return nameDict


print(same_name({"Mary": "Rufus", "Charlie": "Charlie"}))
print(same_name({"Mary": "Rufus", "Charlie": "Spots"}))
print(same_name({"Mary": "Mary", "Charlie": "Charlie"}))

print(dog_name_frequencies({"Mary": "Rufus", "Ryan": "Clifford", "Chloe": "Rufus"}))
print(dog_name_frequencies({}))