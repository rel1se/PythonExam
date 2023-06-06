def main(x):
    my_dict = {1976: {1984: {'TEXT': 0, 'TCSH': 1},
                      2001: 2},
               1965: {1984: {'TEXT': 3, 'TCSH': 4},
                      2001: {'GLSL': 5, 'ABAP': 6}},
               1996: {1984: {'GLSL': 7, 'ABAP': 8},
                      2001: {'TEXT': 9, 'TCSH': 10}}}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main([1984, 'GLSL', 'TCSH', 1996]) == 7)
print(main([1984, 'ABAP', 'TCSH', 1996]) == 8)
print(main([2001, 'GLSL', 'TEXT', 1996]) == 9)
print(main([1984, 'ABAP', 'TEXT', 1965]) == 3)
print(main([1984, 'GLSL', 'TCSH', 1976]) == 1)

