def is_permutation(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False
    for c in str1:
        if c in str2:
            str2 = str2.replace(c, "")
    return len(str2) == 0


s1 = "some          strings    "
s2 = "some   strings"

if __name__ == '__main__':
    is_permute = is_permutation(s1, s2)
    print(is_permute)
