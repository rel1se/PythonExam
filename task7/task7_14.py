def main(l):
    l1 = "000000000"
    l2 = bin(int(l['L2']))[2:].zfill(1)
    l3 = bin(int(l['L3']))[2:].zfill(5)
    l4 = bin(int(l['L4']))[2:].zfill(5)
    l5 = bin(int(l['L5']))[2:].zfill(9)
    l6 = bin(int(l['L6']))[2:].zfill(7)
    return str(int(l6 + l5 + l4 + l3 + l2 + l1, 2))


print(main({'L2': '0', 'L3': '20', 'L4': '18', 'L5': '509', 'L6': '34'}))
print(main({'L2': '1', 'L3': '10', 'L4': '3', 'L5': '464', 'L6': '107'}))