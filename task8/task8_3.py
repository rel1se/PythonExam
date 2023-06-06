# Реализовать функцию для разбора строки, содержащей данные в текстовом формате.
# Изучить детали формата по приведенным ниже примерам.
# Результат вернуть в виде словаря.

def main(text):
    if ('\n' in text):
        text = text.replace('\n', '')
    text = text.replace(" ", '')
    text = text.replace("{{", '')
    text = text.replace("}}", '')
    open = text.count("begin")
    text = text.replace("begin", '')
    text = text.replace("define", '')
    text = text.replace(";end,", '==>')
    keys = []
    values = []
    text = text.split("==>")
    for i in range(open * 2):
        if (i % 2 == 0):
            values.append(text[i])
        else:
            keys.append(text[i])

    temp = dict(zip([data for data in keys], [data for data in values]))
    return temp


text1 = "{{begin define anvege_829==> lace; end,begin define teen_26 ==> ladidi_31; end, begin define xeri_353==>orma_981; end, }}"
print(main(text1))

