def cifra_cesar(texto, pulo, descriptografar=False):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''
    if descriptografar:
        pulo = -pulo
    for caractere in texto.lower():
        if caractere in alfabeto:
            indice = alfabeto.find(caractere)
            novo_indice = (indice + pulo) % 26
            resultado += alfabeto[novo_indice]
        else:
            resultado += caractere
    return resultado

# Teste do Odair
msg = "analista de dados"
chave = 3
print(f"Original: {msg}")
print(f"Cifrado:  {cifra_cesar(msg, chave)}")