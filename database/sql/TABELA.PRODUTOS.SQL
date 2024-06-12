create table IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    Preco FLOAT,
    Quantidade INTEGER NOT NULL
);

INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES ('Banana', 1.99, 2399);
INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES ('Maca', 0.99, 5050);
INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES ('Melancia', 5.99, 3655);
INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES ('Pera', 2.99, 49132);
INSERT INTO Produtos (Nome,Preco,Quantidade) VALUES ('Mamao', 4.99, 89431);


SELECT * FROM Produtos

UPDATE Produtos SET Preco = 4.99 WHERE = id 3;

DELETE FROM Produtos WHERE id =2;

CREATE TABLE IF NOT EXISTS CLIENTES(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    cpf VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(64) UNIQUE NOT NULL,
    numero VARCHAR (20) UNIQUE NOT NULL,
    cep VARCHAR (20) DEFAULT ('')
)

INSERT INTO CLIENTES (nome,cpf,email,numero,cep) VALUES ('samuel','084.810.079-44','samuca@gmail.com','4299223452','85015030');
INSERT INTO CLIENTES (nome,cpf,email,numero,cep) VALUES ('fabricio','084.810.069-42','fabricio10@gmail.com','4299887711','85015123');
INSERT INTO CLIENTES (nome,cpf,email,numero,cep) VALUES ('gabriel','084.810.070-23','gai12@gmail.com','429955664411','85015321');

CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY,
    datapedido DATE NOT NULL,
    Quantidade INTEGER NOT NULL,
    valortotal FLOAT NOT NULL,
    codigodacompra VARCHAR(64) UNIQUE NOT NULL
    Idclientes INTEGER,
    Idpedidos INTEGER,
    FOREIGN KEY (Idclientes) REFERENCES CLIENTES (id),
    FOREIGN KEY (Idprodutos) REFERENCES CLIENTES (id)
    
);

INSERT INTO Pedidos (datapedido,Quantidade,valortotal,codigodacompra,Idclientes,Idpedidos) VALUES ('2024-05-10',5,30,99,'124578936'1,1);
INSERT INTO Pedidos (datapedido,Quantidade,valortotal,codigodacompra,Idclientes,Idpedidos) VALUES ( '2024-05-15',12,100,25,'124578936',2,2);
INSERT INTO Pedidos (datapedido,Quantidade,valortotal,codigodacompra,Idclientes,Idpedidos) VALUES ('2024-05-22',25,350,36,'124578936',3,3);
