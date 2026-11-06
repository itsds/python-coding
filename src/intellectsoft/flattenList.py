# Problem 1

# Input: [1, [2, [3, 4], 5], 6]
# Output: [1, 2, 3, 4, 5, 6]


def flatten(input, output):
    if len(input) == 0:
        print(output)
        return

    for index, i in enumerate(input):
        # print(index)
        # print(i)
        # print(type(i))

        if type(i) == int:
            output.append(i)
            print(output)
        else:
            flatten(input[index:], output)


output = []
input = [1, [2, [3, 4], 5], 6]
result = flatten(input, output)

