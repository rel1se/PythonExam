def main(text):
    text = text.replace('\n', '')
    text = text.replace("[[", '')
    text = text.replace("(", '')
    text = text.replace(" ", '')
    text = text.replace(")", '')
    text = text.replace("]]", '')
    text = text.replace(",", '=:')
    text = text.replace(".", '')
    open = text.count("global")
    text = text.replace("global", '')
    text = text.replace("'", '')
    text = text.split("=:")
    text = text[:-1]
    keys = []
    values = []
    for i in range(open * 2):
        if (i % 2 == 0):
            values.append(text[i])
        else:
            keys.append(text[i])
    temp = dict(zip([data for data in keys], [data for data in values]))
    return temp

print(main("[[(global isgeri =: 'tied_848'.), ( global quaar =:'arceso'.), (global riar =: 'leer_676'.), (global ragein =:'leised'.), ]]"))