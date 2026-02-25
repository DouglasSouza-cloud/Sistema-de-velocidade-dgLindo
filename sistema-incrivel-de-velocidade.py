#Sistema de Velocidade, calcula média e mostra maior/menor velocidade.


velocidades = [] #Lista para guardar os valores inseridos



def media(): #função para calc. média;
    b = sum(velocidades) / len(velocidades)
    print (b)

def maior(): #função para pegar o maior valor;
    a = max(velocidades)
    print(a)

def menor(): #função para pegar o menor valor;
    c = min(velocidades)
    print(c)

def soma(): #Função para somar os valores de velocidade;
    s = sum(velocidades)
    print(s)

print("=== Sistema de Velocidade ===\n")
while True:

        try: 
            velocidades.clear() #limpa a lista ao iniciar o programa novamente;

            for i in range (5): #laço de repetição;
                while True:

                    velo = int(input("Insira velocidade do motor: ")) #entrada de dados do usuário;
                    if velo <0: #Condição para não aceita valor < 0;
                        print("Valor inválido, tente novamente...")
                    else:
                        velocidades.append(velo) #Adiciona os valores inseridos à lista;                     
                        break #Para o looping quando a condição for negada
    

            


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

            ref = str(input("\nDeseja refazer? s/n: \n")) #Decisão do usuário de refazer ou não.
            
            if ref == "s": #Condição
                print("Reiniciando programa...")

            elif ref == "n":
                print("Programa finalizado.")
                break #Para o programa quando a condição for correspondida.

        except ValueError: #Não aceita letras ou diferentes de inteiro.
            print("Digito inválido, tente novamente...")