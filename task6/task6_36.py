def main(x):
    my_dict = {1981: {'LEX': {1966: 0,
                              2016: {'SCSS': 1, 'XTEND': 2},
                              1987: {'SCSS': 3, 'XTEND': 4}},
                      'PAN': 5,
                      'ABNF': {'SCSS': {1966: 6, 2016: 7, 1987: 8},
                               'XTEND': {'LIMBO': 9, 'SLIM': 10}}},
               1975: 11,
               2012: 12}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main([1987, 'ABNF', 'XTEND', 1975, 'LIMBO']))
print(main([2016, 'PAN', 'XTEND', 1981, 'SLIM']))
print(main([1966, 'ABNF', 'XTEND', 2012, 'LIMBO']))
print(main([2016, 'ABNF', 'XTEND', 1981, 'SLIM']))
print(main([2016, 'LEX', 'SCSS', 1981, 'LIMBO']))
