
# Variáveis
valor_total = float(0);
desconto_porcentagem = int(0);
valor_desconto = float(0);
valor_final = float(0);

print("\nO algoritmo calculará o valor de desconto na compra.");

# Input
valor_total = float(input("Digite o valor total: "));
desconto_porcentagem = int(input("Digite a porcentagem de desconto (0 a 100): "));

# Processamento

if ( valor_total < 0 ):
    print("\nO valor da compra é negativo. O cálculo não será efetuado.");
    exit();

if( desconto_porcentagem < 0 or desconto_porcentagem > 100 ) :
    print("\nO valor de desconto deve estar entre 0 e 100.");
    exit();


valor_desconto = valor_total * (desconto_porcentagem / 100);
valor_final = valor_total - valor_desconto;

# Saida de Exercícios
print(f'\nO valor de desconto da compra é: {valor_desconto} R$');
print(f'O valor da compra é: {valor_final} R$');
