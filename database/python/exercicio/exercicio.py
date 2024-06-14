
import os;
import produtos;

inputMenu = int(0);

while( True ):
    os.system('cls');
    print('Menu de Seleção.');
    print('Digite 1 para criar um produto');
    print('Digite 2 para visualizar todos os produtos');
    print('Digite 3 para procurar');
    print('Digite 4 para atualizar');
    print('Digite 5 para excluir');
    print('Digite 0 para encerrar');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 0 ):
        break;
    
    if ( inputMenu == 1 ):
        try:
            name = str('');
            price = float(0);
            quantity = int(0);
        
            print(f'\nDigite os dados solicitados para a criação do produto.');
            name = str(input('Nome: '));
            price = float(input('Preço: '));
            quantity = int(input('Quantidade: '));
        
            response = produtos.create(name,price,quantity);
        
            print(f'{response['message']}');
    
        except:
            print('Something went wrong');

    # SELECT
    if ( inputMenu == 2 ):
        data = [];
        data = produtos.select();

        # Exibir dados corretamente
        if ( data['code'] == 200 ):
            
            for product in data['data']:
                print(f'\nNome: {product[0]} , Preço: {product[1]} R$ , ' + 
                      f'Quantidade: {product[2]} un')

        else:
            # Erro de banco de dados
            if ( data['code'] == 500 ):
                print(f'\n{data['message']}');
            else:
                # Erro não previsto
                print(f'\nUnknown Error');
    
    # FIND
    if ( inputMenu == 3 ):
        data = [];
        name = str('');
        try:
            print('\nProcurar produto específico.');
            name = input('Nome do produto: ');
        
            data = produtos.findByName(name);

            # Exibir dados corretamente
            if ( data['code'] == 200 ):
                print(f'\nNome: {data['data'][0]} , Preço: {data['data'][1]} R$ , ' + 
                      f'Quantidade: {data['data'][2]} un')
            else:
                # Produto não encontrado ou erro de banco de dados
                if ( data['code'] == 404 or data['code'] == 500):
                    print(f'\n{data['message']}');
                else:
                    # Erro não previsto
                    print(f'\nUnknown Error');

        except:
            print('Something went wrong');
    if ( inputMenu == 4 ):
        inputSubMenu = int(0);

        print('\nMenu de atualização.');
        print('Digite 1 para atualizar o nome.');
        print('Digite 2 para atualizar o preço.');
        print('Digite 3 para atualizar a quantidade.');
        try:
            inputSubMenu = int(input('Digite: '));
            if (inputSubMenu == 2):
                name = str('')
                price = float(0);
                print('\n atualizar o preço de um produto.');
                name = input('nome do produto:');
                price = float(input('Novo preço:'));
        
                data = produtos.updatePrice(name ,price);
        
                print(f'\n{data['message']}');

                

            if (inputSubMenu == 3 ):
                name = str('');
                Quantity = int(0);
                print('\nAtualizar a Quantidade dos produtos.')
                name = input('nome do produto: ');
                Quantity =int(input('nova quantidade: '));
    
                data = produtos.updateQuantity(name , Quantity);
    
                print(f'\n{data["message"]}');
     

            if(inputSubMenu == 1 ):
                oldName= str('');
                newName =str('');
                print('\nAtualizar o nome ')
                oldName = input('Nome atual: ')
                newName =  input('Novo nome: ')

                data = produtos.
        except:
            print('something went wrong');
        



    #delete
    if (inputMenu == 5):
        data = [];
        name = str('');

        try:
            print('\nDeletar um produto.');
            name = input('nome do produto');

            data = produtos.delete(name);
            print(f'\n{data['message']}');

        except:
            print('something went wrong');



    input('\nAperte ENTER para continuar.');