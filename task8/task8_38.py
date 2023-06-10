import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace('new', '')
    res = re.findall(r'\w+<==\w+', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].split('<==')
        keys.append(res[i][0])
        values.append(res[i][1])
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    '<: (( new laus <== ceve )) (( new isla_100 <== edan_477 )) (( newusenbi<== onis_718 )) (( new atle_324 <== raaran_892 )) :>'))
