numbers = [];
soma = int(0);
inputnumber = (-1);

print("o algoritmo calculara a soma de todos os numeros.");


#inputs
while (inputnumber != 0):
      print('digite um numero para o vetor. digite 0 para encerrar...')
      inputnumber = int(input("digite:"));

      if (inputnumber == 0):
        break
      
      else:
         numbers.append(inputnumber)

#processamento
for i in range (0 , len(numbers)):
      soma = soma + numbers[i]
     
 
print(f"soma do vetor {numbers}")
print(f"soma do vetor {soma}")     