

keywords = []

def load_keywords():
    """Esta funcion se encarga de leer linea a linea el fichero keywords.txt"""
    with open('keywords.txt') as kw:
        for line in kw:
            keywords.append(line)
        return keywords
        

def show_keywords(keywords):
    for value in keywords:
        print(value)

