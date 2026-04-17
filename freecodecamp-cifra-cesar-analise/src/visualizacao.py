import matplotlib.pyplot as plt

def plotar_frequencia(freq):
    letras = sorted(freq.keys())
    valores = [freq[l] for l in letras]

    plt.bar(letras, valores)
    plt.title("Distribuição de Frequência das Letras")
    plt.xlabel("Letras")
    plt.ylabel("Contagem")
    plt.show()