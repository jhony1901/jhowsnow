
import sqlite3;

connection = sqlite3.connect('Store.db');
cursor = connection.cursor();


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name VARCHAR(32) UNIQUE NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    );
''');

#connection.close();

def create(name:str , price:float , quantity:int):
    try:
        productByName = findByName(name);

        if ( productByName['code'] == 200 ):
            return {'code': 400, 'message': 'Product already exist '};

        cursor.execute('INSERT INTO Products (name,price,quantity) VALUES (?,?,?)', (name , price , quantity));
        connection.commit();
    
        return {'code' : 201 , 'message' : 'Product Created'};
    except:
        return {'code': 500 , 'message' : 'Internal Error'};

def findByName(name:str):
    try:
        cursor.execute('SELECT name,price,quantity FROM Products WHERE name = ?', (name,));
        product = cursor.fetchone();
    
        if ( product == None ):
            return {'code': 404, 'message' : 'Product not found'};
        
        return {'code': 200, 'data': product};

    except:
        return {'code': 500 , 'message' : 'Internal Error'};

def select():
    try:
        products = [];

        cursor.execute('SELECT name,price,quantity FROM Products');
        products = cursor.fetchall();
        return { 'code': 200 , 'data': products};
    
    except:
        return { 'code': 500 , 'message': 'Internal Error'};


def update():
    pass;

def delete(name:str):
    try:
        id = 0;

        cursor.execute('SELECT id FROM Products WHERE name =?',(name,));
        product = cursor.fetchone();

        if(product == None):
            return{'code': 404, 'message': 'product not found'};
    
        id = product[0];
        cursor.execute('DELETE FROM Products WHERE id =?',(id,));
        connection.commit();
        return{'code': 204, 'message': 'Product deleted successfully'}    

    except:
        return{'code': 500 , 'message': 'internal error'};
