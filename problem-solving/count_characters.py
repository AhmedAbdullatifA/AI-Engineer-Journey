def count_characters(string):
    x = set(string)
    y = list(string)
    z = {}

    for i in x:
        if i == ' ':
            continue
        else:
            z[i] = y.count(i)

    return z

print(count_characters("hello python language")) 
# Output: {'h': 2, 'e': 1, 'l': 3, 'o': 2, 'p': 1, 'y': 1, 't': 1, 'n': 2, 'g': 2, 'a': 3, 'u': 1}