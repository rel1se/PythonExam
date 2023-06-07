import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace('"', '')
    res = re.findall(r'-?[0-9]+to\w+', text)
    keys = []
    values = []
    for i in range(len(res)):
        res[i] = res[i].split("to")
        values.append(res[i][0])
        keys.append(res[i][1])
    return dict(zip([data for data in keys], [int(data) for data in values]))

print(main('\begin {{ #2706 to "eren_708"; }}. {{#529 to"tiso";}}. {{#771to"beso_623";}}.{{#-2384 to "leaus"; }}. \end'))