# Adding %20 in empty spaces in a string
input_string = "Mr. hans hammer is a film character  "
string_length = len(input_string)


def URLify(input_str, input_len):
    url = ""
    for i in range(input_len):
        if input_str[i] == " ":
            url += "%20"
        else:
            url += input_str[i]
    return url


print(URLify(input_string, string_length))
