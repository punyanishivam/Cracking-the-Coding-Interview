# IsUnique

# Without any datastructure
def is_unique(input_str):         # Time: O(NlogN) Space: O(1)

    flag = True
    input_str = sorted(input_str)

    for i in range(len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            flag = False

    return flag


# With HashMap
def is_unique1(input_str):        # Time: O(N) Space: O(N)

    from collections import Counter
    str_dict = Counter(input_str)

    for key in str_dict:
        if str_dict[key] > 1:
            return False

    return True


# BitVector approach
def is_unique2(string):            # Time: O(N) Space: O(1)

    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


print(is_unique("akfbuyel"))
