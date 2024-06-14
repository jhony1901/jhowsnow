numeros = [3,1,5,11,10];

print(f"vector inicial{numeros}");

numeros.append(81);
numeros.append(35);

print(f"vector append: {numeros}");

numeros.pop();
numeros.remove(5);

print(f"vector atualizado{numeros}");

print(f"menor numero {min(numeros)}");
print(f"maior numero {max(numeros)}");

numeros.sort();
print(f"numeors ordenados{numeros}");

for count in range (0 , len(numeros) , 1) :
    print(f"vector na posicao [{count}] = {numeros[count]}");