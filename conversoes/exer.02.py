from os import system
#import biblioteca_exer;
from metros import quilometrosmilhas , milhasquilometros;
from temperatura import celsius , fahrenheit;
from medidas import media , comprimento;
#biblioteca_exer.fahrenheit(34)
inputmenu =int(1);
number_1 = float(0);
number_2 = float(0);
number_3 = float(0);
value = float(0);

print (" O menu calcula tres funcoes diferentes.\n ");

while (inputmenu != 0):
     
     system('cls');
     
     print ("Menu de selecão...\n");
     print ("Digite 1 para calcular Metros para Pé...");
     print ("Digite 2 para calcular celsius em fahrenheit...");
     print ("Digite 3 para calcular quilometros em milhas...");
     print ("Digite 0 para encerrar...");
     inputmenu = int(input("Digite:"));
     if (inputmenu == 1):
        print("menu de conversao de medida.");
        print("Digite 1 para converter para metros.");
        print("Digite 2 para converter para pé. ");

        inputmenu = int(input("Digite:"))

        if (inputmenu == 1):
            print("Vamos converter para metros...");
            number_1 = float(input("Digite:"));

            comprimento (number_1);
        
        if (inputmenu == 2 ):
            print ("Vamos converter para pé... ");
            number_1 = float(input("Digite:"));
        
            media (number_1)
        inputmenu = -1

     if (inputmenu == 2 ):
          print("menu de conversao de °c para °f...")
          print ("digite 1 para calcular em fahrenheit...\n ");
          print ("digite 2 para calcular em celsius...")

          inputmenu = int(input("Digite:"));

          if (inputmenu == 1):
            print("vamos calcular fahrenhait para celsius")
            number_2 = float(input("digite:"));
            fahrenheit (number_2);
        
          if (inputmenu == 2):
            print("vamos calcular celsius...");
            number_2 = float(input("Digite:"));
            celsius (number_2);
             
         
          inputmenu = -1

     if (inputmenu == 3):
         print("menu de coversao de quilometros para milhas...");
         print("digite 1 para coverter em quilometros..")
         print("digite 2 para converter para milhas...")
         inputmenu= int(input("digite:"));
         
         if (inputmenu == 1):
          number_3 = float(input("digite:"))
          print("Vamos calcular quilometros para quilometros...\n");
          quilometrosmilhas (number_3);
         

         if (inputmenu == 2):
            print("Vamos converter para milhas...");
            number_3= float(input("Digite"));
            milhasquilometros (number_3)

            inputmenu = -1

     if (inputmenu == 0):
         print(" Menu encerrado...\n");
         exit();

     input ( "digite enter para continua ...\n");