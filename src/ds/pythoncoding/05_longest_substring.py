# Q5: Longest substring without repeating characters
s = "abcabcbb"

def longest_unique(str):
    str_list=[]
    count=0
    for s in str:
        if s not in str_list:
            str_list.append(s)
        else:
            if count < len(str_list):
                count=len(str_list)
            str_list=[]
    return count

print(longest_unique(s))

