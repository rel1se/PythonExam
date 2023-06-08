import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace('#', '')
    text = text.replace('`', '')
    res = re.findall(r'list\((.*?)\)\|>(\w+)', text)
    return [(x[1], x[0].split(';')) for x in res]


print(main('| \begin store list(#3137;#2423; #-6401 ) |> `usa_510; \end. \beginstore list( #8399 ; #818 ; #-1021 ;#-6543 ) |> `anedbe_887;\end.\beginstore list(#-6916; #9659 ) |> `lear_434;\end.|'))