import os ; 
import random;

# variaveis
number = int(0);
value = int (0);
inputmenu = int(1);
sortednumber = int (0);

print(" o algoritmo fara um teste se voce acerta o numero./");
print(" o jogo ira gerar um numero aleatorio de (1 a 100)...\n");
#input
value = int(input( 'digite: ' ));

#processamento
sortednumber = random.randint (1,100);

while (value >= 0 ):
    print ( "menu do jogo.");
    print (f"digite 1 para tentar de novo (voce tem {value} tentativas restantes).");
    print ("digite 0 para desistir do jogo.\n");
    inputmenu = int(input("Digite:"));

    if (inputmenu < 0 or inputmenu > 1 ):
        print ( "DIGITE APENAS NUMEOS PRESENTE NO MENU...");
    else:
        if ( inputmenu == 1 ):
            print ("Vejo que esta determinado !!! vai tenta acerta o numero que escolhi ? Boa sorte.\n");
            number = int(input("digite"));
            value = value - 1 ;
        
            if (number == sortednumber):
                print ("MEUS PARABENS VOCE ACERTOU.");
            
            else :
                print("Errou seu trouxa hahaha");

            if ( number > sortednumber):
                print ("o numero é maior ");
            else:
                print ("o numero é menor");
            
            if (value <= 1):
                print (" GAME OVER ");
                exit();
            
            if ( inputmenu == 0 ):
             print("DESISTIU TAO CEDO, TAO FRACO, ESPERAVA BEM MAIS DE VOCE... VOLTE LOGO (OU NAO/=)");
             exit();
    
    input ("digite enter para continuar...");
    os.system ('cls');

