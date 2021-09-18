p = 194522226411154500868209046072773892801
q = 288543888189520095825105581859098503663
e = 65537
c = 2680665419605434578386620658057993903866911471752759293737529277281335077856

def ExtendedEuclidean(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x
def Carmichael(p, q):
    gcd, x = ExtendedEuclidean(p, q)
    totient = (p // gcd) * (q // gcd)
    return totient
def Euler(p, q):
    return (p - 1) * (q - 1)
# Returns d
def GenerateEPQ(e, p, q):
    N = p * q
    totient = Euler(p, q) # Carmichael or Euler
    gcd, d = ExtendedEuclidean(e, totient)
    return d
# Returns c
def EncryptEMN(e, m, n):
    return pow(m, e, n)
def EncryptEMPQ(e, m, n):
    n = p * q
    return EncryptEMN(e, m, n)
# Returns m
def DecryptCDN(c, d, n):
    return pow(c, d, n)
def DecryptCEPQ(c, e, p, q):
    d = GenerateEPQ(e, p, q)
    n = p * q
    return DecryptCDN(c, d, n)
def DecryptCDPQ(c, d, p, q):
    n = p * q
    return DecryptCDN(c, d, n)

print(bytes.fromhex(hex(DecryptCEPQ(c, e, p, q))[2:]))