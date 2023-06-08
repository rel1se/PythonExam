def main(x):
    my_dict = {1981: {2003: {1973: 0,
                             2012: {'TOML': 1, 'M4': 2, 'HACK': 3},
                             1990: {'TOML': 4, 'M4': 5, 'HACK': 6}},
                      1959: 7,
                      1976: {'TOML': 8, 'M4': 9, 'HACK': 10}},
               2011: 11}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main([2012, 'TOML', 1976, 'LESS', 1981]))
print(main([2012, 'TOML', 1976, 'LESS', 1981]))
print(main([1990, 'M4', 1976, 'LESS', 2011]))
print(main([1973, 'HACK', 1959, 'PLSQL', 1981]))
print(main([1973, 'TOML', 2003, 'PLSQL', 1981]))
print(main([1990, 'M4', 2003, 'PLSQL', 1981]))