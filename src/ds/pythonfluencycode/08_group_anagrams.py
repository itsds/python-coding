# Q8: Group anagrams
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(words):
    group_dict={}
    for word in words:
        sorted_word=''.join(sorted(word))
        if sorted_word not in group_dict:
            group_dict[sorted_word]=[]

    for word in words:
        sorted_word=''.join(sorted(word))
        if sorted_word in group_dict:
            group_dict[sorted_word].append(word)

    return list(group_dict.values())


print(group_anagrams(words))
# expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
