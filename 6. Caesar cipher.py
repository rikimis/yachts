# 6. Caesar cipher

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decode(string, shift, mark = False):
    result = ""
    for char in string:
        if char in abc:
            if mark == False:
                number = abc.index(char) + shift #decode
            else:
                number = abc.index(char) - shift #encode
            if number >= 26:
                number -= 26
            result += abc[number]
        else:
            result += char
    return result

def encode(string, shift):
    return decode(string, shift, True)


print(decode("cas su peniaze", 2)) #ecu uw rgpkcbg
print(encode("ecu uw rgpkcbg", 2)) #cas su peniaze
