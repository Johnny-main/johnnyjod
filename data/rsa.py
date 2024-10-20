import random

def is_probably_prime(candidate, iterations=5):
    if candidate < 2:
        return False
    for small_prime in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if candidate % small_prime == 0:
            return candidate == small_prime
    exponent, remainder = 0, candidate - 1
    while remainder % 2 == 0:
        exponent, remainder = exponent + 1, remainder // 2  # Use // for integer division
    for _ in range(iterations):
        base = pow(random.randint(2, candidate - 1), remainder, candidate)
        if base in (1, candidate - 1):
            continue
        for _ in range(exponent - 1):
            base = pow(base, 2, candidate)
            if base == candidate - 1:
                break
        else:
            return False
    return True

def find_large_prime(bit_length):
    while True:
        prime_candidate = random.getrandbits(bit_length)
        if is_probably_prime(prime_candidate):
            return prime_candidate

def modular_inverse(a, m):
    def extended_gcd(x, y):
        if x == 0:
            return (y, 0, 1)
        else:
            gcd, y1, x1 = extended_gcd(y % x, x)
            return (gcd, x1 - (y // x) * y1, y1)  # Use // for integer division
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Inverse does not exist')
    return x % m

def create_key_pair(bits):
    prime1 = find_large_prime(bits // 2)
    prime2 = find_large_prime(bits // 2)
    modulus = prime1 * prime2
    phi_n = (prime1 - 1) * (prime2 - 1)
    public_exponent = 65537  # Standard value for e
    private_exponent = modular_inverse(public_exponent, phi_n)
    return ((public_exponent, modulus), (private_exponent, modulus))

def encrypt_data(plain_data, pub_key):
    exp, mod = pub_key
    return pow(plain_data, exp, mod)

def decrypt_data(cipher_data, priv_key):
    exp, mod = priv_key
    return pow(cipher_data, exp, mod)

def generate_signature(plain_data, priv_key):
    exp, mod = priv_key
    return pow(plain_data, exp, mod)

def verify_signature(original_data, sig, pub_key):
    exp, mod = pub_key
    return pow(sig, exp, mod) == original_data

if __name__ == "__main__":
    public_key, private_key = create_key_pair(64)
    print(f"Generated Public Key: {public_key}")
    print(f"Generated Private Key: {private_key}")

    message = 32154
    print(f"\nOriginal Message: {message}")

    encrypted_message = encrypt_data(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt_data(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

    signature = generate_signature(message, private_key)
    print(f"\nSignature: {signature}")

    is_signature_valid = verify_signature(message, signature, public_key)
    print(f"Is Signature Valid: {is_signature_valid}")

    tampered_message = 87609
    is_signature_valid = verify_signature(tampered_message, signature, public_key)
    print(f"Is Tampered Message Signature Valid: {is_signature_valid}")
