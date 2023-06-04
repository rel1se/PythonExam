

def main(n):
    n = int(n)
    bitsize = [4, 1, 10, 8]
    bitstart = [sum(bitsize[:i]) for i in range(len(bitsize))]
    arr = ((n >> bitstart[i]) & ((1 << bitsize[i]) - 1)
           for i in range(len(bitstart)))
    arr = ("0x%x" % n for n in arr)
    set = tuple(arr)
    return set