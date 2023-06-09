def main(x):
    bit_size = [10, 8, 10, 7]
    m = []
    for i in range(len(bit_size)):
        if i != 2:
            m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        else:
            m.append(0)
        x = x >> bit_size[i]
    ans = 0
    ans = ans << bit_size[3]
    ans += m[3]
    ans = ans << bit_size[0]
    ans += m[0]
    ans = ans << bit_size[2]
    ans += m[2]
    ans = ans << bit_size[1]
    ans += m[1]
    return str(hex(ans))


print(main(16345819042))
print(main(3095379218))
print(main(9053986735))
print(main(17211033731))
