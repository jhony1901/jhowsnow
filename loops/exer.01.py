import os;
# Contador e limite da repetição da tabuada
counter = int(1);
limit = int(10);
# Variáveis para calcular a tabuada
value = int(0);
result = int(0);
# Variáveis do Menu de seleção
inputMenu = int(1);

print('O algoritmo fará a tabuada do número digitado.');

while ( inputMenu != 0 ):
    print("\nMenu de seleção !!\n");
    print("Digite 1 para calcular a tabuada.");
    print("Digite 2 para alterar as regras da tabuada.");
    print("Digite 0 para encerrar a operação.");

    inputMenu = int(input("Digite: "));

    if ( inputMenu == 1 ):
        valuei = int(input("digite um numero:" ))
        print("\nVAMOS CALCULAR A TABUADA...\n");
        for counter in range ( 1, limit +1, 1 ):
              result = value * counter
              print (f"{value} X {counter} = {result}");
    
    if ( inputMenu == 2 ):
        print("\nA tabuada por padrão calcula de 1 até 10.")
        print(f'Atualmente, ela está calculando de {counter} até {limit}');
        limit = int(input("Digite um novo limite para a tabuada: "));

    if ( inputMenu == 0 ):
        print("Encerrando...");
        exit();


    input ('DIGITE ENTER PARA CONTINUAR...');
    os.system( 'cls' );