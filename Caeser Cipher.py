def caesar_cipher(text, shift):
    result = ""

    for char in text:
        # Encrypting uppercase characters
        if char.isupper():
            result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        # Encrypting lowercase characters
        elif char.islower():
            result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            result += char

    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, shift)

text = "Extraordinary"
shift = 5
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_decipher(encrypted_text, shift)

print("Text: " + text)
print("Shift: " + str(shift))
print("Cipher: " + encrypted_text)
print("Decipher: " + decrypted_text)
