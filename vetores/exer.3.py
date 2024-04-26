number = [];
inputnumber = int(-1);
sam = int(0);
count = int(0);

print ("O algoritmo calculara a media do vetor");

while (inputnumber != 0):
     print('digite numeros para o vetor. Digite 0 para encerrar.');
     inputnumber = int(input("digite:"));

     if (inputnumber == 0):
        break

     else:
        number.append(inputnumber);

for i in range (0 , len(number)):
    sam = number + number
    print(f"{count}")

count = sam / len(number)
print (f"{count}")