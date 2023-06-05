def main(n):
    bitsize = [3, 5, 9, 7, 2]
    bitstart = [sum(bitsize[:i]) for i in range(len(bitsize))]
    arr = ((n >> bitstart[i]) & (1 << bitsize[i] - 1)
           for i in range(len(bitsize)))
    arr = ("0x%x" % n for n in arr)
    res = []
    for i in arr:
        tmp = ("M" + str(arr. + 1), i)
        res.append(tmp)
    return res

print(main(3502792))
