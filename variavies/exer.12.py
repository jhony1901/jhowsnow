#variavies
number_1 = int(0);
number_2 = int(0);
result = int(0);

#informacao
print ("\no algorimo verificara se os numeros sao divisiveis.\n");

#processamento
number_1 = int(input("digite"));
number_2 = int(input("digite"));
 
#conta
result = number_1 % number_2

#inforcao final
if (result == 0):
   print ("sim é divivel\n");
else :
   print("nao é divisivel");