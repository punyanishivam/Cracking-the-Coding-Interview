# URLify

# Built-In function
def urlify(input_str):          # Time: O(n) Space: O(1)
    return input_str.replace(" ", "%20")


print(urlify("Mr John Smith"))
