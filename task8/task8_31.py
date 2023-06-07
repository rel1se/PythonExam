import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    res = re.findall(r'\w+\)to\w+', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].split(')to')
        values.append(res[i][0])
        keys.append(res[i][1])
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    '<sect> <block>glob q(ceso) to laan_787. </block>. <block>globq(usti_739)to edte. </block>. <block> glob q(soza_264) to edaror_173.</block>. </sect>'))
