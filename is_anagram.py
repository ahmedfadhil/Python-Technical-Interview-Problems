input_str1 = "practice makes perfect"
input_str2 = "perfect makes practice"

input_str3 = "allergy"
input_str4 = "allergic"


# An anagram is when the two strings share the same characters
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    dict1 = dict.fromkeys(list(alphabets), 0)
    dict2 = dict.fromkeys(list(alphabets), 0)

    for i in range(len(str1)):
        dict1[str1[i]] += 1
        dict2[str2[i]] += 1
    return dict1 == dict2


if __name__ == '__main__':

    # Driver code
    print("is anagram? ", is_anagram(input_str1, input_str2))
    print("is anagram? ", is_anagram(input_str3, input_str4))

# Notice sorting could be used as well
# # vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
#
# # sort the vowels
# vowels.sort()
#
# # print vowels
# print('Sorted list:', vowels)
