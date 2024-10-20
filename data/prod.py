def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def columnar_transposition(text, key):  
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    columns = [''] * len(key)
    
    for i, char in enumerate(text):
        columns[i % len(key)] += char
    
    return ''.join(columns[i] for i in key_indices)

def product_cipher_encrypt(plaintext, caesar_shift, transposition_key):
    # Step 1: Substitution (Caesar Cipher)
    substituted_text = caesar_cipher(plaintext, caesar_shift)
    
    # Step 2: Transposition (Columnar Transposition)
    ciphertext = columnar_transposition(substituted_text, transposition_key)
    
    return ciphertext

def product_cipher_decrypt(ciphertext, caesar_shift, transposition_key):
    # Reverse the transposition
    key_indices = sorted(range(len(transposition_key)), key=lambda k: transposition_key[k])
    num_cols = len(transposition_key)
    num_rows = len(ciphertext) // num_cols
    remainder = len(ciphertext) % num_cols
    
    columns = [''] * num_cols
    start = 0
    
    for index in key_indices:
        length = num_rows + 1 if index < remainder else num_rows
        columns[index] = ciphertext[start:start + length]
        start += length
    
    transposed_text = ''.join([columns[i % num_cols][i // num_cols] for i in range(len(ciphertext))])
    
    # Reverse the substitution
    decrypted_text = caesar_cipher(transposed_text, -caesar_shift)
    
    return decrypted_text

# Example usage:
plaintext = input("enter plain text: ")
caesar_shift = int(input("Enter the shift number: "))
transposition_key = input("Enter the transposition key number format: ")
print("Plain text:",plaintext)
print("Shift:",caesar_shift)
print("Transposition Key:",transposition_key)

ciphertext = product_cipher_encrypt(plaintext, caesar_shift, transposition_key)
print("\nCiphertext:", ciphertext)

decrypted_text = product_cipher_decrypt(ciphertext, caesar_shift, transposition_key)
print("\nDecrypted Text:", decrypted_text)