# Реализовать функцию для вычисления дерева решений:
def main(x):
    my_dict = {'YACC': {1957: {1993: 0, 2013: 1, 1967: 2},
                        2014: 3},
               'GLSL': {1957: {1993: 4,
                               2013: {1971: 5, 2009: 6, 1994: 7},
                               1967: {'ATS': 8, 'UNO': 9}},
                        2014: 10}}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main(['UNO', 2009, 1957, 1967, 'YACC']) == 2)
print(main(['UNO', 1971, 1957, 1967, 'GLSL']) == 9)
print(main(['UNO', 1971, 2014, 1993, 'GLSL']) == 10)
print(main(['UNO', 1994, 1957, 1993, 'YACC']) == 0)
print(main(['ATS', 2009, 1957, 1967, 'GLSL']) == 8)
