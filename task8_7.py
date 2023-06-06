import re


def main(text):
    if '\n' in text:
        text = text.replace('\n', '')
    text = text.replace('"', '')
    text = text.replace(' ', '')
    result = re.findall(r'option(\w+)<\|list\((.*?)\)', text)
    return [(x[0], x[1].split(';')) for x in result]


print(main(
    '<block> { option "eronve"<|list(sorain ; gezala ; enered ); }. {option "soquen_815" <| list( soma_663 ;istear_93;oratti; ares_278); }.{option"anxe" <| list( reedin ;atonra_168);}. </block>'))
