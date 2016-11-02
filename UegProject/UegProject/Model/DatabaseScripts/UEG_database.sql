CREATE DATABASE UEG;

USE UEG;

CREATE TABLE tb_Cargo(
Cargo varchar(30) NOT NULL,
Cargo_id smallint NOT NULL AUTO_INCREMENT,
PRIMARY KEY(Cargo_id)
);

insert into tb_cargo(cargo) values('Prefeito');
insert into tb_cargo(cargo) values('Vereador');
insert into tb_cargo(cargo) values('Governador');
insert into tb_cargo(cargo) values('Presidente');
insert into tb_cargo(cargo) values('Senador');
insert into tb_cargo(cargo) values('Deputado');

CREATE TABLE tb_Pais(
Pais_id smallint NOT NULL AUTO_INCREMENT,
Pais varchar(100) NOT NULL,
PRIMARY KEY(Pais_id)
);

CREATE TABLE tb_Estado(
Estado_id smallint NOT NULL AUTO_INCREMENT,
Estado varchar(100) NOT NULL,
Pais_id smallint NOT NULL,
PRIMARY KEY(Estado_id),
FOREIGN KEY(Pais_id) REFERENCES tb_Pais(Pais_id)
);


CREATE TABLE tb_Cidade(
Cidade_id smallint NOT NULL AUTO_INCREMENT,
Cidade varchar(100) NOT NULL,
Estado_id smallint NOT NULL,
PRIMARY KEY(Cidade_id),
FOREIGN KEY(Estado_id) REFERENCES tb_Estado(Estado_id)
);

insert into tb_Pais(Pais) values('Brasil');

insert into tb_Estado(Estado, Pais_id) values('Sao Paulo', 1);
insert into tb_Estado(Estado, Pais_id) values('Rio de Janeiro', 1);


insert into tb_Cidade(Cidade, Estado_id) values('Sao Paulo', 1);
insert into tb_Cidade(Cidade, Estado_id) values('Sao Bernardo do Campo', 1);
insert into tb_Cidade(Cidade, Estado_id) values('Rio de Janeiro', 2);



CREATE TABLE tb_Eleitor
(
CPF int,
Nome varchar(100) NOT NULL,
Cidade_id smallint NOT NULL,
URL varchar(2000),
Votou boolean NOT NULL,
PRIMARY KEY(CPF),
foreign key fk_eleitor(Cidade_id) REFERENCES tb_Cidade(Cidade_id)
);

CREATE TABLE tb_Candidato
(
CPF int,
Numero int NOT NULL,
Cargo_id smallint NOT NULL,
Cidade_id smallint,
Estado_id smallint,
Pais_id smallint NOT NULL,
Votos int NOT NULL,
Apelido varchar(100),
PRIMARY KEY(CPF),
UNIQUE KEY(Numero, Cargo_id),
FOREIGN KEY(CPF) REFERENCES tb_Eleitor(CPF),
foreign key (Cargo_id) REFERENCES tb_cargo(Cargo_id),
FOREIGN KEY(Pais_id) REFERENCES tb_Pais(Pais_id),
FOREIGN KEY(Estado_id) REFERENCES tb_Estado(Estado_id),
FOREIGN KEY(Cidade_id) REFERENCES tb_Cidade(Cidade_id)
);

insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos) values(3, 33, 1, 2, 1, 1, 0);
insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos) values(4, 3333, 2, 2, 1, 1, 0);
insert into tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) values(5, 11, 4, 1, 0);
insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos) values(2, 111, 3, 2, 1, 1, 0);
insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos) values(1, 3333, 6, 2, 2, 1, 0);
CREATE TABLE tb_UEV
(
Usuario varchar(50),
Senha varchar(50) NOT NULL,
Cidade_id smallint NOT NULL,
Ativo boolean NOT NULL,
PRIMARY KEY(Usuario),
foreign key (Cidade_id) REFERENCES tb_Cidade(Cidade_id)
);

insert into tb_uev (usuario, senha, cidade_id, Ativo) values ('user1', 'senha1', 2, false);
insert into tb_uev (usuario, senha, cidade_id, Ativo) values ('user2', 'senha2', 3, false);

