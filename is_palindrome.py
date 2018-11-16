import string


def is_palindrome(s):
    s = s.lower()
    translator = str.maketrans('', '', string.punctuation)
    s = s.translate(translator)
    s = s.replace(" ", "")
    return s == s[::-1]


str1 = "Dammit I'm mad"
str2 = "Race Car"
str3 = "I am upset"

if __name__ == '__main__':
    palindrome = is_palindrome(str1)
    print(palindrome)
