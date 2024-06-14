
bimestre_1 = float(0);
bimestre_2 = float(0);
bimstre_3 = float(0);
bimestre_4 = float(0);
resultado = float(0);

print("o algoritmo vai informar se o aluno passara de ano.\n");


bimestre_1 = float(input("digite a nota:"));
bimestre_2 = float(input("digite um numero:"));
bimstre_3= float(input("digite um numero:"));
bimestre_4 = float(input("digite um numero:"));

resultado = (bimestre_1 + bimestre_2 + bimstre_3 + bimestre_4) / 4

print (f"a nota do aluno é {resultado}");

if (resultado >=6):
    print("\o aluno esta aprovado ");
    exit();
else :
    print ("o aluno reprovou");
    
    


