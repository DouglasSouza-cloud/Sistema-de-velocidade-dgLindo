import time

velocidades = []  # Lista para guardar os valores inseridos

def media():  # Função para calc. média;
    b = sum(velocidades) / len(velocidades)
    print(b)

def maior():  # Função para pegar o maior valor;
    a = max(velocidades)
    print(a)

def menor():  # Função para pegar o menor valor;
    c = min(velocidades)
    print(c)

def soma():  # Função para somar os valores de velocidade;
    s = sum(velocidades)
    print(s)

print("=== Sistema de Velocidade Iniciando... ===\n")
time.sleep(2)
while True:

    try:
        velocidades.clear()  # Limpa a lista ao iniciar o programa novamente;

        for i in range(5):  # Laço de repetição;
            while True:

                velo = int(input("Insira velocidade do motor: ")) # Entrada de dados do usuário;
                time.sleep(1) 
                if velo < 0:  # Condição para não aceitar valor < 0;
                    print("Valor inválido, tente novamente...")
                else:
                    velocidades.append(velo)  # Adiciona os valores inseridos à lista;
                    break  # Para o looping quando a condição for negada

        print("===Relatório final===\n")

        print("Velocidades inseridas: ", velocidades)

        print("\nMédia Aritmética das velocidades: ")
        media()

        print("\nMaior velocidade: ")
        maior()

        print("\nMenor velocidade: ")
        menor()

        print("\nValor total das velocidades: ")
        soma()

        ref = str(input("\nDeseja refazer? s/n: \n"))  # Decisão do usuário de refazer ou não.

        if ref == "s":  # Condição
            print("Reiniciando programa...")
            time.sleep(2)  # Aguarda 2 segundos antes de reiniciar

        elif ref == "n":
            print("Programa finalizado.")
            break  # Para o programa quando a condição for correspondida.

    except ValueError:  # Não aceita letras ou diferentes de inteiro.
        print("Digito inválido, tente novamente...")