
#variaveis
valortotal = float(0);
desconto =  int(0);
resultado = float(0);

# print
print ("\no algoritmo calcula a porcentagem do desconto.");

# processamento
valortotal = float (input("valor total:"));
print (f"o valortotal da compra ficol {valortotal}");
desconto = int (input("desconto"));
# calculo do desconto
desconto = ( valortotal * desconto) /100;
resultado =(valortotal - desconto)
# informacao final da conta
print (resultado)
print (f"\no desconto do cliente deu {desconto}");
print (f"\no resultado do desconto deu {resultado}");


