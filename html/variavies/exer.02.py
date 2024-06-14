nota_1 = float(0);
nota_2 = float(0);
nota_3 = float(0);
resultado = float(0);

print ("O algoritmo calculara a nota a partir dos dados informados.");

nota_1 = float(input("nota1:"));
nota_2 = float(input("nota2:"));
nota_3 = float(input("nota3:"));

resultado = (nota_1 + nota_2 + nota_3) / 3;

print(resultado)
print(f"a soma das notas sao :{resultado}");