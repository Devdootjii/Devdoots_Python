def encrypt_message(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_value = ord(char)
            shifted_value = ascii_value + shift
            encrypt_char = chr(shifted_value)
            encrypted_text += encrypt_char
        else:
            encrypted_text += char

    return encrypted_text
