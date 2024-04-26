import random;
from os import system;
player = int(0);
sortednumber = int(0);
selectmenu = int (0);
inputmenu = int (0);
somapontos = int(0);
dicas = int(5);


print ('Bem vindo ao jogo da adivinhacão.');
print ("Vamos as regras...");
print ('Um numero aleatorio sera gerado de acordo com a dificuldade.');
print ('O jogador tera 5 tentativas para dar uma forca');
print ('o jogador tera 4 tentativas.');
print("menu de selecão do jogo.");
print("vamos para as dificuldades !");
print('digite 1 modo facil apresenta numeros entre (1 e 30).');
print('digite 2 modo médio apresente numeros entre (1 e 50)');
print('digite 3 modo dificil apresenta numeros entre (1 e 100)');

selectmenu = int(input("digite."))

if (selectmenu == 1 ):
        print("voce escolhel modo facil");
        sortednumber = random.randint(1 , 30);
       

if (selectmenu == 2):
        print("voce escolhel modo medio");
        sortednumber = random.randint(1 , 50);
             

if (selectmenu == 3):
        print("mvoce escolheu modo dificil");
        sortednumber = random.randint (1 , 100);
    
while (True):
    print('digite 1 para jogar 2 para dar dicas 3 para sair da partida.')

    inputmenu = int(input("digite."))
        
    if (inputmenu == 1):
          player = int(input("digite sua tentiva"))
          

          if (player == sortednumber):
            print("acertou")
          else:
                print("tente novamente")

          somapontos = somapontos -1     
        
    if (inputmenu == 2):
        print(f"esta maior que o numero.")
        dicas = (dicas > sortednumber)
        print(f"esta menor que o numero.")
        dicas = dicas - 1
        dicas =(dicas < sortednumber)         
    if (inputmenu == 3):
        print("O jogo nem comecou e ja saiu...Mais sorte na proxima vez...");
        break;
    
    somapontos = somapontos -1
    dicas = dicas - 1
    
    input("aperte Enter para continuar...")