def main(x):
    my_dict = {1990: {2020: {'OZ': 0, 'FANCY': 1, 'LATTE': 2},
                      1976: {'OZ': 3, 'FANCY': 4, 'LATTE': 5},
                      1989: 6},
               1996: {2020: 7,
                      1976: 8,
                      1989: {'ORG': 9, 'M4': 10}}}
    while isinstance(my_dict, dict):
        for i in x:
            if i in my_dict.keys():
                my_dict = my_dict[i]
                break
    return my_dict


print(main([2020, 'FANCY', 'M4', 1990]) == 1)
print(main([2020, 'LATTE', 'ORG', 1996]) == 7)
print(main([1976, 'LATTE', 'ORG', 1996]) == 8)
print(main([1976, 'LATTE', 'ORG', 1990]) == 5)
print(main([1976, 'OZ', 'M4', 1990]) == 3)
