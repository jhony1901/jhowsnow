vt = [];
sam =int(0);
inputnumber =int(-1);

print("O algoritmo calculara a soma do vetor apartir dos numeros inseridos.");

while (inputnumber != 0):
    print("digite um numero para vetor.digite 1 para encerrar.");
    inputnumber = int(input("Digite:"));

    if (inputnumber == 0):
        break

    else:
        vt.append(inputnumber)

#processamento
vt = max(vt)

print(f"maior numero digitado. {vt}");
