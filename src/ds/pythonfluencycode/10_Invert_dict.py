# Q10: Invert a dict with duplicate values
d = {"a": 1, "b": 2, "c": 1}

def invert_dict(d):
    output_dict={}

    for k,v in d.items():
        list_l = []
        if v not in output_dict:
            list_l.append(k)
            output_dict[v]=list_l
        else:
            output_dict[v].append(k)

    return output_dict


print(invert_dict(d))
# expected: {1: ['a', 'c'], 2: ['b']}
