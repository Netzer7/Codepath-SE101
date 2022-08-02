import time

def has_duplicates(my_list):
    '''
    Return True if there are any duplicates in the list my_list and False otherwise.
    '''
    for item1 in my_list:
        count = 0
        for item2 in my_list:
            if item1 == item2:
                count += 1
        if count > 1:
            return True
    return False

def has_duplicates_dict(my_list):
  myDict = {}
  for item in my_list:
    if item in myDict:
      return True
    else:
      myDict[item] = 1
  return False
  
# Test Cases
my_list = [1, 2, 3, 3, 4, 2, 2, 1, 3, 2]
start_time = time.time()
list_result = has_duplicates(my_list)
end_time = time.time()
total_time = end_time - start_time
print("List Implementation")
print("Input:", my_list)
print("Output:", list_result)
print("Time", total_time)


start_time = time.time()
dict_result = has_duplicates_dict(my_list)
end_time = time.time()
total_time = end_time - start_time

print("/nDictionary Implementation")
print("Input:", my_list)
print("Output:", dict_result)
print("Time", total_time)