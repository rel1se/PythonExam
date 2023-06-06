import re


def main(text):
    if ('\n' in text):
        text = text.replace('\n', '')
    text = text.replace('"', '')
    text = text.replace(' ', '')
    result = re.findall(r'@(\w+)<\|list\((.*?)\)', text)
    return [(x[0], x[1].split(';')) for x in result]

print()