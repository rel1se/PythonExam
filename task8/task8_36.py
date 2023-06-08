import re


def main(text):
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace("'", '')
    res = re.findall(r'decllist\((.*?)\)\=>(\w+)', text)
    return [(x[1], x[0].split(',')) for x in res]


print(main(
    "[<section> decl list( 'teries', 'sovema' )=> enteus;</section>;<section> decl list( 'geerra' , 'riaed','isre','tieron_939' ) => ceusdi_386; </section>; <section>decllist('raace_874' , 'anlebe', 'anra', 'beenle') => radi_712;</section>;]"))
