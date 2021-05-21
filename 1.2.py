# Check Permutation

# With HashMaps
def check_permutation(str1, str2):       # Time: O(N) Space: O(N)

    from collections import Counter
    return Counter(str1) == Counter(str2)


print(check_permutation("rotor", "trroo"))
