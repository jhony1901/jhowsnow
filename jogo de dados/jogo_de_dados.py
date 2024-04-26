# Importações
import time;
from random import randint;
from os import system;

# Declaração de Variáveis
soma_jogador_1 = int(0);
soma_jogador_2 = int(0);
inputMenu = int(0);
inputMenuPlayer = int(0);
sortedNumber = int(0);

# Print Explicativo
print("Bem vindo ao Jogo de Dados !!");
print("Regras:");
print("Os 2 jogadores deverão jogar dados somando seus valores.");
print("A soma não pode ultrapassar 21, portanto, é possível parar de jogar quando desejar.");
print("O jogador que atingir 21 ou conseguir o maior valor ganha.");

input("\nAperte ENTER para continuar.");
# Processamento
def menuDoJogador( nomeJogador:str , soma_pontos:int ):
    
    print(f"\nMenu do {nomeJogador}.");
    print("Digite 1 para jogar ou 2 para passar a sua vez.");
    
    inputMenuPlayer = int(input("Digite: "));

    if (inputMenu == 0):
        print ("Achei que voce era mais do isso.... :/")
    
    
    if (inputMenuPlayer == 1):
        sortedNumber = randint(1 , 6);

        soma_pontos = soma_pontos + sortedNumber;

        print(f'Você tirou {sortedNumber} no dado. A soma ficou em {soma_pontos}');
 
        if ( soma_pontos == 21 ):
            print('Voce foi excelente, chegou em 21. Muito bom ...');
        
        if ( soma_pontos > 21 ):
            print('\nOps voce passou de 21 tenta da proxima vez. bye bye hahahah...\n');
            print('Game Over para o jogador 1');
                
                
            
    if (inputMenuPlayer == 2):
        print("\nDesistiu tão cedo?? hahaha que covarde");
          
    return soma_pontos;
    # Processamento
while(True):
    system('cls');

    print("Menu do Jogo.");
    print("Digite 1 para Jogar.");
    print("Digite 0 para encerrar");

    inputMenu = int(input("Digite: "));

    if (inputMenu == 0):
        break;
    
    if (inputMenu == 1):
        print('\nAtualmente, a tabela de pontuações está desta forma:');
        print(f'Jogador 1: {soma_jogador_1} pontos // Jogador 2: {soma_jogador_2} pontos');
    
        soma_jogador_1 = menuDoJogador('Jogador 1' , soma_jogador_1);
    
        soma_jogador_2 = menuDoJogador('Jogador 2', soma_jogador_2);


    input("\nAperte ENTER para continuar.");