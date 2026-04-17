def cifra_cesar(text, shift, decrypt=False):
    result = ''

    if decrypt:
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result