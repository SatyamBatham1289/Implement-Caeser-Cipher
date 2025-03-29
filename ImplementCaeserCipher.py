def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():  # Encrypt only letters
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    
    return result

# User Input
message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

# Process message
output = caesar_cipher(message, shift, mode)
print(f"\n{mode.capitalize()}ed message: {output}")
