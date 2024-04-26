import time;
from random import randint;
from os import system;
pontosplayer = int(0);
pontoscomputer = int(0);
inputmenu = int(0);
inputmenuplayer = int(0);
sortednumber = int(0);
impate = int(0);

print ("Benvindo ao jogo de pedra,papel e tesoura.");
print ("regras");
print ("Os jogadores iram jogar, quem chegar a cinco pontos primeiro ganha...");

input ("Aperte ENTER para continua");
def gamepo (p1:str ,p2:int):
    global round
      
    if (inputmenuplayer == 1 and sortednumber == 2 ):
        print('voce escolheu papel, mais eu escolhi tesoura, voce perdeu.hahaha...');
        pontoscomputer = pontoscomputer + 1
    if (inputmenuplayer == 2 and sortednumber ==1):
        print('voce escolheu tesoura, eu escolhi papel,eu perdi. hehehe');
        pontosplayer = pontosplayer +1
    if (inputmenuplayer == 3 and sortednumber == 2):
        print('voce escolheu pedra, eu escolhi tesoura, entao eu perdi.ifififi');
        pontosplayer = pontosplayer +1
    if (inputmenuplayer == 1 and sortednumber == 3):
        print('voce escolheu papel, eu escolhi pedra, perdi de novo.');
        pontosplayer = pontosplayer +1
    if (inputmenuplayer == 3 and sortednumber == 1):
        print('voce escolheu pedra e eu escolhi papel entao eu ganhei. hahahah');
        pontoscomputer = pontoscomputer +1
    if (inputmenuplayer == 2 and sortednumber ==3):
        print('voce escolheu tesoura e eu escolhi pedra entao eu ganhei. hahahah');
        pontoscomputer = pontoscomputer +1;
 
    if (inputmenu == 1):
            round = 3;
while(True):
    system('cls');

    print("MENU DO JOGO")
    print('DIGITE 1 PARA JOGAR.');
    print('DIGITE 0 PARA DESISTIR.');

    inputmenu = int(input('Digite:'));
    if(inputmenu == 0):
        print('ACHEI QUE TINHA ENCONTRADO UM RIVAL A ALTURA MAIS NAO, VOCE ME DECEPCIONOU...');
        break

    if(inputmenu == 1):
        print('Digite 1 para papel 2 para tesoura 3 pedra.');
        inputmenuplayer = int(input('Digite:'));

        if(inputmenuplayer == 1):
            print('papel')

        if(inputmenuplayer == 2):
            print('tesoura')

        if(inputmenuplayer == 3):
            print('pedra')

        sortednumber = randint (1,3);
    

        if (inputmenuplayer == sortednumber):
            print('empatou');
            impate = impate -1

            pontosplayer = pontosplayer + 1
            pontoscomputer = pontoscomputer +1
            impate = impate -1
        if (pontosplayer == 5 ):
            print (f"VOCE CONSEGUIU PARABENS {pontosplayer}!!!");
        if (pontoscomputer == 5):
            print (f"Nao foi desta vez eu GANHEI {pontoscomputer}!!!");
        
        gamepo
    input("\nAperte ENTER para continuar.");