import sqlite3;

comand = str('');
result = [];

Connection = sqlite3.connect('./bamco.db');

cursor = Connection.cursor();

cursor.execute (
   ' create table IF NOT EXISTS Produtos (' +
   ' id INTEGER PRIMARY KEY,' +
   ' nome VARCHAR(64) NOT NULL,' +
   ' Preco FLOAT,' +
   ' Quantidade INTEGER NOT NULL);'
);
cursor.execute ('INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES(?,?,?)', ('Banana', 1.99, 2399));
Connection.commit

comand = cursor.execute('SELECT * FROM Produtos')
result = comand.fetchall();

print(result);