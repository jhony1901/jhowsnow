create table IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    idade INTEGER,
    email VARCHAR(64) NOT NULL
);
-- funbcoes do crud

-- c / insert:
INSERT INTO clientes(nome,idade,email) VALUES ('ROBERTO' ,27 ,'TROBERTO.9165@GMAIL.COM');

-- r / select:
SELECT * FROM clientes;

-- PARA APAGAR A TABELA, USE O COMANDO :
DROP TABLE clientes;
SELECT nome,idade,email FROM CLIENTES;

-- u / update
UPDATE clientes SET idade = 23 WHERE id = 1;
