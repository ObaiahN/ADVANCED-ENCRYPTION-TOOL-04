from cryptography.fernet import Fernet

# Step 1: Generate a secret key
key = Fernet.generate_key()
print("Generated Key:", key.decode())

# Step 2: Create a cipher object
cipher = Fernet(key)

# Step 3: Original message
message = "Advanced Encryption Tool Example"
print("Original Message:", message)

# Step 4: Encrypt the message
encrypted_message = cipher.encrypt(message.encode())
print("Encrypted Message:", encrypted_message)

# Step 5: Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()

OUTPUT:-
Generated Key: M2JoZ0RjOEdhckJsbHZ3ZG93bmRzODJiT0p2T2sxQUM=
Original Message: Advanced Encryption Tool Example
Encrypted Message: b'gAAAAABkX1pD...'
Decrypted Message: Advanced Encryption Tool Example
print("Decrypted Message:", decrypted_message).
