#Write a Python function to find the length of the longest substring without repeating characters. Your solution should have O(n) time complexity.

#Input:



#Expected Output:

#3

def get_length(s):
    return_list=[]
    count=0
    for i in range(len(s)):
        if s[i] not in return_list:
            return_list.append(s[i])
        else :
            if count < len(return_list):
                count=len(return_list)
            return_list=[]

    return count

s = "abcabcbb"
print(get_length(s))