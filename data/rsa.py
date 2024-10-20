def gcd(a, b):
    """Calculate the greatest common divisor using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_exp(base, exp, mod):
    """Perform modular exponentiation."""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply the base with result
            result = (result * base) % mod
        exp //= 2  # Divide exp by 2
        base = (base * base) % mod  # Square the base
    return result

def mod_inverse(e, phi):
    """Calculate the modular inverse using the Extended Euclidean Algorithm."""
    t1, t2 = 0, 1
    r1, r2 = phi, e
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2
    if r1 == 1:
        return t1 % phi
    return -1  # Modular inverse does not exist

def main():
    # Input the plaintext and primes
    pt = int(input("Enter the secret message (plaintext) to encrypt: "))
    p = int(input("Enter a prime number P: "))
    q = int(input("Enter a prime number Q: "))

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = next(i for i in range(2, phi) if gcd(i, phi) == 1)

    # Calculate d
    d = mod_inverse(e, phi)
    if d == -1:
        print("No modular inverse found for the given e.")
        return

    # Encrypt the plaintext
    ct = mod_exp(pt, e, n)

    # Output the keys and ciphertext
    print(f"\nPublic Key (n, e) = ({n}, {e})")
    print(f"Private Key (d) = {d}")
    print(f"Ciphertext (CT): {ct}")

    # Decrypt the ciphertext
    pt2 = mod_exp(ct, d, n)
    print("\nDecrypting...")
    print(f"Decrypted Plaintext (PT): {pt2}")

if __name__ == "__main__":
    main()
