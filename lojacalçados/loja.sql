CREATE TABLE if NOT EXISTS funcionario(
    id INTEGER PRIMARY KEY,
    Nome VARCHAR(64) NOT NULL,
    cpf  VARCHAR (64) UNIQUE NOT NULL,
    Contato VARCHAR (64) UNIQUE NOT NULL,
    Cep VARCHAR (64) DEFAULT,
    Comissao INTEGER NOT NULL
)

CREATE TABLE if NOT EXISTS Clientes(
    id INTEGER PRIMARY KEY,
    Nome VARCHAR(64) NOT  NULL,
    Cpf VARCHAR(64) UNIQUE NOT NULL,
    Contato VARCHAR(64) UNIQUE NOT NULL,
    Email VARCHAR(84) UNIQUE NOT NULL,
    Cep VARCHAR(20) DEFAULT
)
CREATE TABLE if NOT EXISTS Calcados(
    id INTEGER PRIMARY KEY,
    Marca VARCHAR(64), 
    Numeracao VARCHAR(64) NOT NULL,
    Preco FLOAT NOT NULL,
    Modelo VARCHAR(65)
)
CREATE TABLE if NOT EXISTS Estoque(
    id INTEGER PRIMARY KEY,
    Quantidade INTEGER NOT NULL,
    Codigo VARCHAR(64) UNIQUE NOT NULL,
    idcalcado INTEGER,
    FOREIGN KEY (idcalcado) REFERENCES Calcados(id)
)
CREATE TABLE if NOT EXISTS Venda(
    id INTEGER PRIMARY KEY,
    datacompra DATE NOT NULL,
    Quantidade INTEGER NOT NULL,
    valortotal FLOAT NOT NULL,
    codigodacompra VARCHAR(64) UNIQUE NOT NULL,
    idclientes INTEGER,
    idcalcado INTEGER
    FOREIGN KEY (idclientes) REFERENCES Clientes(id)
    FOREIGN KEY (idcalcado) REFERENCES Calcados(id)
)
CREATE TABLE if NOT EXISTS vendafuncionario(
    id INTEGER PRIMARY KEY,
    Comissao INTEGER NOT NULL,
    idvenda INTEGER,
    idfuncionario INTEGER,
    FOREIGN KEY (idvenda) REFERENCES venda(id),
    FOREIGN KEY (idfuncionario) REFERENCES funcionario(id)

)