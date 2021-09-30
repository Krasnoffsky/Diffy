import lab1 as lib


if __name__ == '__main__':

    a = 3
    e = 12345678
    m = 27644437
    print("Pow = ", lib.FastAsFakPow(a, e, m), "\n")

    a = 28
    b = 19
    #print("Euclide = ", lib.EuclideAl(a, b), "\n")

    a = 7
    b = 13
    res1, res2 = lib.Diffy(a, b)
    #print("zAB = ", res1, "\nzBA = ", res2, "\n")

    a = 2
    p = 23
    y = 9
#print("LittleBigStep = ", lib.LittleBigStep(a, p, y))
