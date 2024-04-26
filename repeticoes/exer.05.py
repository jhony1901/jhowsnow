import time 
#variaveis 
next_number = int(0);
number_1 = int(0);
number_2 = int(1);

print ("o algoritmo vai gerar uma seguencia de fibonacci.");

number = int(input("digite um numero"));

print ( number_1)
print ( number_2)

while   next_number <= 100 :
       next_number = number_1 + number_2 
       number_1 = number_2 
       number_2 = next_number

       print (next_number)
       time.sleep (1) 
    

    