# s = ({2000, 2015, "APL"},
#      {2000, 2015, "TXL", 2005},
#      {2000, 2015, "TXL", 1983},
#      {2000, 2015, "GDB", 2005},
#      {2000, 2015, "GDB", 1983},
#      {2000, 2017, "APL", 2013},
#      {2000, 2017, "APL", 1979},
#      {2000, 2017, "APL", 2015},
#      {2000, 2017, "TXL", 2005},
#      {2000, 2017, "TXL", 1983},
#      {2000, 2017, "GDB"},
#      {2013})
#
#
# def main(x):
#     s1 = set(x)
#     return [i for i in range(len(s))
#             if not (len(s[i] - s1))][0]
def main(x):
    my_dict = {2000: {2015: {'APL': 0,
                             'TXL': {2005: 1, 1983: 2},
                             'GDB': {2005: 3, 1983: 4}},
                      2017: {'APL': {2013: 5, 1979: 6, 2015: 7},
                             'TXL': {2005: 8, 1983: 9},
                             'GDB': 10}},
               2013: 11}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main(['APL', 2000, 2017, 2005, 1979]) == 6)
print(main(['TXL', 2000, 2017, 1983, 1979]) == 9)
print(main(['GDB', 2000, 2015, 1983, 1979]) == 4)
print(main(['GDB', 2013, 2015, 1983, 2013]) == 11)
print(main(['GDB', 2000, 2017, 1983, 2015]) == 10)
