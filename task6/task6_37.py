def main(x):
    my_dict = {'SELF': {2007: {'POD': 0,
                               'GAMS': {'IOKE': 1, 'FANCY': 2}},
                        1969: {'IOKE': {2012: 3, 1996: 4, 1984: 5},
                               'FANCY': {'POD': 6, 'GAMS': 7}},
                        1970: {'POD': {2012: 8, 1996: 9, 1984: 10},
                               'GAMS': 11}},
               'STATA': 12}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main(['FANCY', 1984, 1969, 'GAMS', 'SELF']) == 7)
print(main(['FANCY', 2012, 2007, 'POD', 'STATA']) == 12)
print(main(['FANCY', 1996, 2007, 'POD', 'SELF']) == 0)
print(main(['IOKE', 1984, 2007, 'GAMS', 'SELF']) == 1)
print(main(['FANCY', 1996, 1970, 'GAMS', 'SELF']) == 11)
