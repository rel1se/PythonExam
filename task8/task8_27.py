import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    res = re.findall(r'\w+<==\w+', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].split('<==')
        keys.append(res[i][0])
        values.append(res[i][1])
    return dict(zip([data for data in keys], [data for data in values]))


print(main('( [[gean_230<== ceat_38 ]], [[ leisdi_38 <== teorbe]], )'))
