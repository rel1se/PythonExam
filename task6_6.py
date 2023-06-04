s = ({2002, 'DIFF', 2014, 'M'},
     {2002, 'DIFF', 2014, 'NL'},
     {2002, 'DIFF', 2014, 'COBOL'},
     {2002, 'DIFF', 1994, 'M'},
     {2002, 'DIFF', 2014, 'NL'},
     {2002, 'DIFF', 2014, 'COBOL'},
     {2002, 'LFE'},
     {2002, 'KRL'},
     {1976, 'DIFF', 2014},
     {1976, 'DIFF', 1994},
     {1976, 'LFE'},
     {2002, 'KRL'},
     {1963})


def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not (len(s[i] - s1))][0]


main([1994, 'NL', 'LFE', 1970, 2002])
# print(main([2014, 'M', 'KRL', 2007, 1963]))