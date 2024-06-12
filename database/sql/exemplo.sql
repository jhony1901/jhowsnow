create table IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    idade INTEGER,
    email VARCHAR(64) UNIQUE NOT NULL
);
-- funbcoes do crud

-- c / insert:
INSERT INTO clientes(nome,idade,email) VALUES ('mateus' ,22 ,'mateus.9165@GMAIL.COM');
INSERT INTO clientes(nome,idade,email) VALUES ('claudia' ,33 ,'claudia.9165@GMAIL.COM');
INSERT INTO clientes(nome,idade,email) VALUES ('gustavo' ,40 ,'gustavo.9165@GMAIL.COM');

-- APAGAR TABELA
DROP TABLE CLIENTES;

-- r / select:
SELECT * FROM clientes;

-- PARA APAGAR A TABELA, USE O COMANDO :
DROP TABLE clientes;
SELECT nome,idade,email FROM CLIENTES;
SELECT nome,idade,email FROM clientes WHERE email ='claudia.9165@GMAIL.COM';

-- u / update

update clientes set idade = 20
UPDATE clientes SET idade = 22 WHERE id = 1;
UPDATE clientes SET idade = 33 WHERE id = 2;
UPDATE clientes SET idade = 40 WHERE id = 3;

DELETE FROM clientes WHERE id = 1;

-- ALTERRAR COLUA --
ALTER TABLE clientes ADD COLUNM biografia VARCHAR(300);
