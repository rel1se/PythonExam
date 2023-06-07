import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace('dostoreq', '')
    text = text.replace('#', '')
    res = re.findall(r'\(\w+\)islist\([-?\w+,?]+\)', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].replace('(', '')
        res[i] = res[i].replace(')', '')
        res[i] = res[i].split('islist')
        keys.append(res[i][0])
        values.append(res[i][1])
    res_values = []
    for i in range(len(values)):
        values[i] = values[i].split(',')
        for j in range(len(values[i])):
            values[i][j] = int(values[i][j])
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    '<section>do store q(riesge)is list( #-9261,#-4531 , #3866 , #-2539 )done. do store q(iszaan) is list( #-3448 ,#-6377 ,#413) done. do storeq(anonbe) is list( #7384 ,#7796) done. do store q(anerza_406)is list(#1772,#-1155, #-8174 , #9175 )done. </section>'))
