import time
number_1 = int(0);
number_2 = int(0);
number_3 = int(0);

def media( n1:int, n2:int, n3:int ):
   
    result = float(0);

    

    result = (n1 + n2 + n3) / 3
    print(f"media: {result}")


#explicacao 
print("o algoritmo fara o calculo da media de 3 numero.")

#input
number_1 = int(input("digite: "));
number_2 = int(input("digite: "));
number_3 = int(input("digite: "));

print("funcao em execucao...");
time.sleep(1);
media(number_1, number_2, number_3 );


#media(3 ,6, 9)
#media (10 ,9 ,21)