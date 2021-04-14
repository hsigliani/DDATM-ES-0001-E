import sys


# replace any character with the next in the alphabet. Next for 'z' is 'a'
def replace(text):
    result = ''

    for c in text:
        n = ord(c)

        # means the character is in 'A..Y' or 'a..y'
        # so replace with next in the sequence
        if (65 <= n < 90) or (97 <= n < 122):
            result += chr(n + 1)

        # means the character is 'Z' or 'z'
        # so replace with 'a' or 'A'
        elif n == 90 or n == 122:
            result += chr(n - 25)

        # any other not in 'A..Z' or 'a..z'
        else:
            result += c

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python main.py \'<some text>\'')
    else:
        print(replace(sys.argv[1]))
