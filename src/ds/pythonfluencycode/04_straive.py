# Q4: Character count dictionary
s = "banana"

def char_count(s):
    count_dict={}
    for ch in s:
        if ch in count_dict:
            count_dict[ch]+=1
        else:
            count_dict[ch]=1
    return count_dict


print(char_count(s))
# expected: {'b': 1, 'a': 3, 'n': 2}
