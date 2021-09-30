from array import array
import random


def FastAsFakPow(a, e, m):

    result = 1
    bin_e = DecToBin(e)
    last_num = a % m

    if (bin_e % 10 == 1):
        result = (result * last_num) % m

    bin_e = bin_e // 10

    while (bin_e != 0):

        last_num = (last_num * last_num) % m
        if (bin_e % 2 == 1):
            result = (result * last_num) % m

        bin_e = bin_e // 10

    return result


def EuclideAl(a, b):
    U = array('i', [a, 1, 0])
    V = array('i', [b, 0, 1])
    T = array('i', [0, 0, 0])
    q = 0

    while V[0] != 0:
        q = U[0] // V[0]
        T[0] = U[0] % V[0]
        T[1] = U[1] - q * V[1]
        T[2] = U[2] - q * V[2]
        U[0] = V[0]
        U[1] = V[1]
        U[2] = V[2]
        V[0] = T[0]
        V[1] = T[1]
        V[2] = T[2]

    return U


def Diffy(keyA, keyB):

    p = SimpleGenerator()
    q = int((p - 1) / 2)
    g = random.randint(2, p)

    while (FastAsFakPow(g, q, p) == 1):
        g = random.randint(2, p)

    print("p = ", p, " g = ", g)

    yA = FastAsFakPow(g, keyA, p)
    yB = FastAsFakPow(g, keyB, p)

    zAB = FastAsFakPow(yB, keyA, p)
    zBA = FastAsFakPow(yA, keyB, p)

    return (zAB, zBA)


def LittleBigStep(a, p, y):

    x = 0

    while True:
        m = random.randint(1, p)
        k = random.randint(1, p)
        while m * k <= p:
            m = random.randint(1, p)
            k = random.randint(1, p)

        print("m = ", m, " k = ", k)

        mI = array('i', [])
        mJ = array('i', [])
        g = False

        for i in range(m):
            mI.append((FastAsFakPow(a, i, p) * y) % p)

        for j in range(1, k + 1):
            mJ.append(FastAsFakPow(a, m * j, p))
            if mJ[j - 1] in mI:
                i = mI.index(mJ[j - 1])
                g = True
                break

        if g:
            x = i * m - j
            if FastAsFakPow(a, x, p) == y:
                break

    return x


def DecToBin(dec):

    bin = 0
    last_bit = 0
    k = 1

    while (dec != 0):
        last_bit = dec & 1
        bin = bin + last_bit * k
        dec = dec >> 1
        k = k * 10

    return bin


def GCD(a, b):

    r = 0
    while(b != 0):
        r = a % b
        a = b
        b = r

    return a


def isPrime(p):
    if p <= 1:
        return False

    b = int(p ** 0.5)

    for i in range(2, b + 1):
        if p % i == 0:
            return False

    return True


def SimpleGenerator():

    lim = 100
    res = random.randint(1, lim)

    while not (isPrime(res) and isPrime(int((res - 1) / 2))):
        res = random.randint(1, lim)

    return res
