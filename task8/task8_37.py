import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace('"', '')
    res = re.findall(r'\w+=>[a-z]+', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].split('=>')
        keys.append(res[i][1])
        values.append(res[i][0])
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    'do begin store @"aorrixe" => solebe. end,begin store @"anen" =>veeses. end, begin store @"isla_437" => ledi. end, done'))
print(main(
    'o begin store @"soaveza_701" => enxe_840. end,begin store @"abece"=>edqule. end, begin store @"sola_510"=> tela. end, done'))
