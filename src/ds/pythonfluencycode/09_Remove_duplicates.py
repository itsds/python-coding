# Q9: Remove duplicates, keep order
nums = [3, 1, 3, 2, 1]

def dedupe(nums):
    return_list=[]
    for num in nums:
        if num not in return_list:
            return_list.append(num)
    return return_list


print(dedupe(nums))
# expected: [3, 1, 2]
