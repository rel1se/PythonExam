def main(q):
    q1 = bin(int(q['Q1'], 16))[2:].zfill(1)
    q2 = bin(int(q['Q2'], 16))[2:].zfill(3)
    q3 = bin(int(q['Q3'], 16))[2:].zfill(8)
    q4 = bin(int(q['Q4'], 16))[2:].zfill(6)
    q5 = bin(int(q['Q5'], 16))[2:].zfill(5)
    return str(int(q5 + q4 + q3 + q2 + q1, 2))

print(main({'Q1': '0x1', 'Q2': '0x6', 'Q3': '0xb1', 'Q4': '0x20', 'Q5': '0x19'}))
