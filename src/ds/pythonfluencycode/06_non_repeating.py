# Q6: First non-repeating character
s = "swiss"

def first_unique(s):
    char_count={}
    for i in s:
        if i not in char_count:
            char_count[i]=1
        else:
            char_count[i]+=1

    for i in s:
        if char_count[i]==1:
            return i

    return ""

print(first_unique(s))
# expected: 'w'
