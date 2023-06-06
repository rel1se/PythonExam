def main(x):
    my_dict = {'EQ': {1990: {'PAWN': 0, 'RUBY': 1, 'COBOL': 2},
                      1981: {1976: 3, 1989: 4, 2012: 5},
                      1998: {1976: 6, 1989: 7, 2012: 8}},
               'HACK': 9,
               'XOJO': 10
               }
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main(['EQ', 1976, 1981, 'COBOL']) == 3)
print(main(['HACK', 1989, 1998, 'COBOL']) == 9)
print(main(['EQ', 1989, 1990, 'COBOL']) == 2)
print(main(['EQ', 1976, 1998, 'PAWN']) == 6)
print(main(['EQ', 2012, 1981, 'COBOL']) == 5)
