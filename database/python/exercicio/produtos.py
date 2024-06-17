
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


def updatePrice(name:str , price:float):
    try:
        id = 0;

        cursor.execute('SELECT id FROM Products WHERE name =?',(name,));
        Product = cursor.fetchone();

        if(Product == None):
            return{'code': 404, 'message': 'product not found'};
    
        id = Product[0];
        cursor.execute('UPDATE Products SET price=? WHERE id =?',(price,id));
        connection.commit();
        return{'code': 202, 'message': 'Product update successfully'}    

    except:
        return{'code': 500 , 'message': 'internal error'};
        

def updateQuantity(name:str , Quantity:int):
    try:
        cursor.execute('SELECT id from Products WHERE name =?',(name,));
        Product = cursor.fetchone();

        if(Product == None):
            return{'code': 404, 'message': 'product not found'};
    
        id = Product[0];

       

        cursor.execute('UPDATE  Products SET quantity=?  WHERE id =?',(Quantity,id));
        connection.commit();
        return{'code': 202, 'message': 'Product update successfully'}    

    except:
        return{'code': 500 , 'message': 'internal error'};
def updateName (oldName:str , newName:str):
    try:
        cursor.execute('SELECT id from Products WHERE name =?',(oldName,));
        Product = cursor.fetchone();

        if(Product == None):
            return{'code': 404, 'message': 'product not found'};

        id = Product[0];

        ProductByname = findByName(newName) ;
        
        if (ProductByname ['code']== 200):
            return {'code': 400,'messag': 'Product name already exist'};
    
        cursor.execute('UPDATE  Products SET name=?  WHERE id =?',(newName,id));
        connection.commit();

        return{'code': 202, 'message': 'Product update successfully'}     
    except:
         return{'code': 500 , 'message': 'internal error'};
def delete(name):
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
