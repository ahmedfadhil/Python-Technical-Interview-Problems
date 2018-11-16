import string


def is_string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # using hash table
    dict1 = dict.fromkeys(list(string.ascii_lowercase), 0)
    dict2 = dict.fromkeys(list(string.ascii_lowercase), 0)

    for i in range(len(str1)):
        dict1[str1[i]] += 1
        dict2[str2[i]] += 1
    return dict1 == dict2


if __name__ == '__main__':
    test_str1 = "water bottle"
    test_str2 = "elttob retaw"

    test_str3 = "different string"
    test_str4 = "yet another different string"

    test_str5 = "yet another"
    test_str6 = "yet differs"
    print(is_string_rotation(test_str1, test_str2))
    print(is_string_rotation(test_str3, test_str4))
    print(is_string_rotation(test_str5, test_str6))
