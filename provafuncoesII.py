#Desenvolva um programa em Python que funcione como um processador de texto simples. O programa deverá realizar diversas operações em um texto fornecido, incluindo:

#Contar palavras
#Contar letras
#Inverter o texto
#Substituir palavras-chave
#Requisitos:
#Crie uma função chamada processador_texto que aceite uma string de texto como argumento.

#A função também deve aceitar uma série de operações através de argumentos de palavra-chave usando **kwargs. As operações que podem ser realizadas incluem:

#"contar_palavras": Contar o número de palavras no texto.
#"contar_letras": Contar o número de letras no texto (desconsiderando espaços).
#"inverter_texto": Inverter o texto de entrada.
#"substituir_palavra": Substituir uma palavra específica no texto por uma nova palavra.
#Utilize funções lambda para realizar as operações de acordo com as palavras-chave especificadas nos argumentos de **kwargs.

#Para a operação de substituição de palavras, a função deve aceitar palavras adicionais: uma palavra a ser substituída (por exemplo, substituir_palavra) e uma nova palavra (por exemplo, nova_palavra).

#A função deve aplicar todas as operações em sequência e retornar o texto resultante após todas as operações.

# Funções lambda para cada operação

def processador_texto(texto, **kwargs):
    operacoes = {
        "contar_palavras": lambda t: len(t.split()),
        "contar_letras": lambda t: sum(1 for c in t if c.isalpha()),
        "inverter_texto": lambda t: t[::-1],
        "substituir_palavra": lambda t, antiga, nova: t.replace(antiga, nova),
    }

    resultado = texto

    for operacao, parametros in kwargs.items():
        if operacao == "contar_palavras":
            print(f"Número de palavras: {operacoes[operacao](resultado)}")
        elif operacao == "contar_letras":
            print(f"Número de letras: {operacoes[operacao](resultado)}")
        elif operacao == "inverter_texto" and parametros:
            resultado = operacoes[operacao](resultado)
        elif operacao == "substituir_palavra" and isinstance(parametros, tuple):
            antiga, nova = parametros  # Extraindo as palavras da tupla
            resultado = operacoes[operacao](resultado, antiga, nova)

    return resultado

# Exemplo de uso
texto_inicial = "A Infinity School tem ótimos cursos."

# Aplicando operações no texto
resultado_final = processador_texto(
    texto_inicial,
    contar_palavras=True,
    contar_letras=True,
    substituir_palavra=("ótimos", "exelentes"),  # Substituir "ótimos" por "exelentes"
    inverter_texto=True
)

print(texto_inicial)
print("Texto final:", resultado_final)
