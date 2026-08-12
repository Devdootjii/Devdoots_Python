ef encrypt_message(text, shift):
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

def decrypt_message(encrypted_text, shift):
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():
            ascii_value = ord(char)
            shifted_value = ascii_value - shift
            decrypt_char = chr(shifted_value)
            decrypted_text += decrypt_char
        else:
            decrypted_text += char
    return decrypted_text
text = "DEVDOOT"
shift = 3
encrypted = encrypt_message(text, shift)
print("Encrypted:", encrypted)
decrypted = decrypt_message(encrypted, shift)
print("Decrypted:", decrypted)
