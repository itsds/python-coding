# Q7: Two Sum
nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    output_list=[]
    num_dict={}
    for num in nums:
        req=target-num
        if req in nums:
            output_list.append(num)
            output_list.append(req)
            break

    return output_list

print(two_sum(nums, target))
# expected: [0, 1]