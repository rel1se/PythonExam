def main(x):
    bit_size = [4, 1, 10, 8]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(int(x))[2:][-bit_size[i]::], 2))
        x = int(x) >> bit_size[i]
    return tuple([hex(m[i]) for i in range(len(m))])


print(main('3029662'))