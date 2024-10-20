import hashlib
def generate_md5(message):
    md5_hash = hashlib.md5()
    md5_hash.update(message.encode('utf-8'))
    return md5_hash.hexdigest()

original_message = input("Enter the message: ")
original_hash = generate_md5(original_message)
print(f"Original Message: {original_message}")
print(f"MD5 Hash: {original_hash}")
modified_message = input("Enter the modified message (or press Enter to keep it the same): ")
if modified_message.strip() == "":
    modified_message = original_message
modified_hash = generate_md5(modified_message)
print(f"Modified Message: {modified_message}")
print(f"MD5 Hash of Modified Message: {modified_hash}")
if original_hash == modified_hash:
    print("Integrity Check Passed: The message has not been altered.")
else:
    print("Integrity Check Failed: The message has been altered.")
