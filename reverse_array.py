def reverse_list(num_list, start, end):
    # Write your code here
    if end >= len(num_list):
        return num_list
    reverseList = []
    for num in num_list[start:end+1]:
        reverseList.append(num)
        num_list.remove(num)
    reverseList.reverse()
    if len(num_list) != 0:
        return reverseList + num_list
    return reverseList