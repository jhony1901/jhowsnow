import time 
#variaveis
number = int(0);
multiplicador = int(1);
result = int(0);

print ("o algoritmo vai resolver uma tabuada.");

number = int(input("digite um numero"));
 

while (multiplicador <= 10):
      result= number * multiplicador
      print (f"{number}x {multiplicador}= {result}");
      time.sleep(1)
      multiplicador = multiplicador + 1 ;
      
      



