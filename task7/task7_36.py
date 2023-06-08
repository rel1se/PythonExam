def main(x):
    bit_size = [10, 8, 5, 6]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2::][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    ans = 0
    ans = ans << bit_size[2]
    ans += m[2]
    ans = ans << bit_size[3]
    ans += m[3]
    ans = ans << bit_size[1]
    ans += m[1]
    ans = ans << bit_size[0]
    ans += m[0]
    return ans


print(main(394991413))
print(main(368865962))