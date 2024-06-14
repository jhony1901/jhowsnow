#variaveis

number = int(0);
result = float(0);
result2 = float(0);
#informacao
print ("o algoritmo vai verificar se o numero digitado é divisivel por 3 e 5.\n");

#procesamento
number = int(input("digite um numero\n"))

result = number % 3 
result2 = number % 5

#informacao final
if (result == 0 and result2 == 0):
    print (f"\no numero informado e divisivel por 3 e 5.\n");

else :
    print("nao é divisivel");