from src.cifra import cifra_cesar
from src.analise import frequencia_letras
from src.visualizacao import plotar_frequencia

texto = "Analista de Dados em transição de carreira"

cifrado = cifra_cesar(texto, 3)

print("Texto original:", texto)
print("Texto cifrado:", cifrado)

freq = frequencia_letras(cifrado)

plotar_frequencia(freq)