import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace('var', '')
    res = re.findall(r'-?[0-9]+|\w+', text)
    keys = []
    values = []
    for i in range(len(res)):
        if i % 2 == 0:
            values.append(res[i])
        else:
            keys.append(res[i])
    return dict(zip([data for data in keys], [data for data in values]))


print(main('<<{{ var #-5211 |> tiin }} {{ var #-3119 |> riain_443 }} >>'))
print(main('<<{{var #-8396 |>maeses }} {{ var #1009 |> lerier_668}}{{ var #2111|>qua }} >>'))