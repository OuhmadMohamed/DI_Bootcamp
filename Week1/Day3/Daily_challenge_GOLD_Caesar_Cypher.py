###  Daily challenge GOLD: Caesar Cypher

### Daily challenge GOLD: Caesar Cypher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift inside alphabet range (0–25)
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces and punctuation
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Reverse shift for decryption


print("Welcome to Caesar Cipher!")
choice = input("Type 'encrypt' or 'decrypt': ").lower()

message = input("Enter your message: ")
shift = int(input("Enter shift number: "))

if choice == "encrypt":
    print("Encrypted message:", encrypt(message, shift))
elif choice == "decrypt":
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
