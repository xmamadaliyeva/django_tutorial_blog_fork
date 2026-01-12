def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

p = int(input("Enter p: "))
q = int(input("Enter q: "))
h = int(input("Enter h (private key): "))
x = int(input("Enter x (public key): "))
k = int(input("Enter k (random nonce): "))
H_m = int(input("Enter H(m) (hash of message): "))

r = pow(x, k, p) % q       # r = (x^k mod p) mod q
k_inv = modinv(k, q)       # k^-1 mod q
s = (k_inv * (H_m + h * r)) % q  # s = k^-1 * (H(m) + h*r) mod q

print(f"\nDSA Signature: (r, s) = ({r}, {s})")

y = pow(x, h, p)

# 1. w = s^-1 mod q
w = modinv(s, q)

# 2. u1 = H(m) * w mod q
u1 = (H_m * w) % q

# 3. u2 = r * w mod q
u2 = (r * w) % q

# 4. v = ((g^u1 * y^u2) mod p) mod q
v = ((pow(x, u1, p) * pow(y, u2, p)) % p) % q

print(f"\nVerification value v = {v}")

if v == r:
    print("Imzo to'g'ri (valid)")
else:
    print("Imzo noto'g'ri (invalid)")
