def f22(x):
    F = x & 0xC0000000
    E = x & 0x20000000
    D = x & 0x10000000
    C = x & 0xE000000
    B = x & 0x1FFFE00
    A = x & 0x1FF

    B <<= 7
    E >>= 14
    A <<= 6
    C >>= 22
    D >>= 26
    F >>= 30

    x = A + B + C + D + E + F
    return x


print(f"f(0x708d850f) = {f22(1888322831)}")
print(f"f(0xbafd838e) = {f22(3137176462)}")
