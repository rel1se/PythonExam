import re


def main(text):
    if '\n' in text:
        text = text.replace('\n', '')
    r = r"-?\d*\sto\s[0-9A-Za-z_]*"
    z = re.findall(r, text)
    keys = []
    values = []
    for i in z:
        arr = i.split(" to ")
        values.append(int(arr[0]))
        keys.append(arr[1])
    return dict(zip([data for data in keys], [data for data in values]))



print(main('(( .begin auto 6023 to abi_276. .end. .begin auto -7450 to iscela_703..end. ))'))
print(main('(( .begin auto -4942 to zaso. .end. .begin auto -4816 to diis. .end..begin auto 1372 to antige_235. .end. .begin auto -2167 to onbi_884..end.))'))