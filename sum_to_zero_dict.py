import time

def sum_to_zero(my_list):
    '''
    Find two elements from my_list which sum to zero.
    Return a tuple of the two elements if they exist and None otherwise.
    '''
    for item1 in my_list:
        for item2 in my_list:
            if item1 + item2 == 0:
                return item1, item2
    return None

def sumZero(my_list):
  myDict = {}
  for item in my_list:
    myDict[item] = True
  for item in my_list:
    if -item in my_list:
      return item, -item
  return None
  
# Test Cases
my_list = [4, 5, -7, -3, 8, -4]
start_time = time.time()
list_result = sum_to_zero(my_list)
end_time = time.time()
total_time = end_time - start_time
print("List Implementation")
print("Input:", my_list)
print("Output:", list_result)
print("Time", total_time)


start_time = time.time()
dict_result = sumZero(my_list)
end_time = time.time()
total_time = end_time - start_time

print("/nDictionary Implementation")
print("Input:", my_list)
print("Output:", dict_result)
print("Time", total_time)