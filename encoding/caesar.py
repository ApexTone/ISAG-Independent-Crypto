def encode_caesar(line: str, shift: int):
    if shift < 1:
        raise Exception('Shift amount must be > 0')

    output = ""
    for character in line:
        if character.isupper():
            shifted_ascii = ord('A')+((ord(character)-ord('A') + shift) % 26)
        elif character.islower():
            shifted_ascii = ord('a')+((ord(character)-ord('a') + shift) % 26)
        else:
            shifted_ascii = ord(character)
        output += chr(shifted_ascii)
    return output


if __name__ == '__main__':
    print(encode_caesar('1234567890!', 1))

    print(encode_caesar('QUIck browns fox juMP OVER Lazy dog', 1))
    print(encode_caesar('QUIck browns fox juMP OVER Lazy dog'.upper(), 1))
    print(encode_caesar('QUIck browns fox juMP OVER Lazy dog'.lower(), 1))

    print(encode_caesar('QUIck browns fox juMP OVER Lazy dog', 0))
    print(encode_caesar('QUIck browns fox juMP OVER Lazy dog', -2))
