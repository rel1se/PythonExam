def main(s):
    keys = []
    values = []
    for i in range(len(s)):
        keys.append(s[i][0])
        values.append(s[i][1])
    smap = dict(zip([data for data in keys], [data for data in values]))

    s1 = bin(int(smap['S1']))[2::].zfill(2)
    s2 = bin(int(smap['S2']))[2::].zfill(3)
    s3 = bin(int(smap['S3']))[2::].zfill(4)
    s4 = bin(int(smap['S4']))[2::].zfill(2)
    s5 = bin(int(smap['S5']))[2::].zfill(7)
    return str(int(s5 + s4 + s3 + s2 + s1, 2))


print(main([('S1', '0'), ('S2', '6'), ('S3', '0'), ('S4', '3'), ('S5', '28')]))
print(main([('S1', '2'), ('S2', '2'), ('S3', '2'), ('S4', '0'), ('S5', '42')]))