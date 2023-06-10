def main(x):
    x = int(x, 16)
    bit_size = [4, 4, 9, 7, 2]
    m = []
    for i in range(len(bit_size)):
        if i != 3:
            m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        else:
            m.append(0)
        x = x >> bit_size[i]
    ans = 0
    ans = ans << bit_size[0]
    ans += m[0]
    ans = ans << bit_size[3]
    ans += m[3]
    ans = ans << bit_size[4]
    ans += m[4]
    ans = ans << bit_size[1]
    ans += m[1]
    ans = ans << bit_size[2]
    ans += m[2]
    return ans


def main2(x):
    bit_size = [4, 2, 6, 1, 7, 9]
    x = int(x, 16)
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    return dict(zip(['C' + str(i + 1) for i in range(len(m))], [str(i) for i in m]))


def main3(x):
    u1 = bin(x['G1'])[2:].zfill(10)
    u2 = bin(x['G2'])[2:].zfill(5)
    u3 = "000000"
    u4 = bin(x['G4'])[2:].zfill(7)
    u5 = bin(x['G5'])[2:].zfill(9)
    return int(u5 + u4 + u3 + u2 + u1, 2)


# print(main('0x2eee87a'))
# print(main2('0x1693883d'))
# print(main3([('U1', '94'), ('U2', '603'), ('U3', '1'), ('U4', '2'), ('U5', '0')]))
print(main3({'G1': 968, 'G2': 12, 'G4': 118, 'G5': 181}))