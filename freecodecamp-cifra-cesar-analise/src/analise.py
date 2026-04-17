from collections import Counter

def frequencia_letras(texto):
    letras = [c.lower() for c in texto if c.isalpha()]
    return Counter(letras)