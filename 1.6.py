# String compression

def string_compression(input_str):      # Time: O(N)  Space: O(N)

    count = 1
    result = []

    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            result.append(input_str[i] + str(count))
            count = 1

    result.append(input_str[-1] + str(count))
    return "".join(result)


print(string_compression("aabcccccaa"))
