#SISTEMA SIMPLES DE SUPERVISÃO DE PRODUÇÕES.

import time

periodos = [] 

def media():  # Função para calc. média;
    b = sum(periodos) / len(periodos)
    print(b)

def maior():  # Função para pegar o maior valor;
    a = max(periodos)
    print(a)

def menor():  # Função para pegar o menor valor;
    c = min(periodos)
    print(c)


while True:
        print("\n=== Sistema de supervisão ===\n") 

        try:
            periodos.clear()  # Limpa a lista ao iniciar o programa novamente;

            for i in range(5):  # Laço de repetição;
                while True:

                    quant = int(input("\nDigite a quantidde de peças produzidas: \n")) # Entrada de dados do usuário;

                    if quant <= 0:  # Condição para não aceitar valor < 0;
                        print("\nValor inválido, tente novamente...")
                    else:
                        periodos.append(quant)  # Adiciona os valores inseridos à lista;
                        break  # Para o looping quando a condição for negada;


            print("\n---RELATÓRIO FINAL---\n")
            print("\nTotal de peças Produzidas por hora:", sum(periodos), "Peças")
            print("\nMédia da Produção de peças por hora:") 
            media() #Chamando a função de média
            print("\nMaior valor da Produção: ") 
            maior() #Chamando a função de maior valor
            print("\nMenor valor da Produção: ")
            menor() #Chamando a função de menor valor
            
        
            ref = str(input("\nDeseja refazer? s/n: \n"))  # Decisão do usuário de refazer ou não.

            if ref == "s":  # Condição
                print("Reiniciando programa...")
                time.sleep(2)  # Aguarda 2 segundos antes de reiniciar

            elif ref == "n":
                print("Programa finalizado.")
                break  # Para o programa quando a condição for correspondida.
        
        except ValueError:
            print("\nDigito inválido, É permitido apenas números.")
            print("Tente Novamente...\n")