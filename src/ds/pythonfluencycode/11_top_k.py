# Q11: Top-k frequent words
text = "the cat and the hat and the bat"
k = 2

def top_words(text, k):
    str_arr=text.split(" ")
    str_dict={}
    for str in str_arr:
        if str not in str_dict:
            str_dict[str]=1
        else:
            str_dict[str]+=1

    result=sorted(str_dict.items(), key= lambda x:x[1], reverse=True)[:k]
    return result


print(top_words(text, k))
# expected: [('the', 3), ('and', 2)]
