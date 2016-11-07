import mysql.connector
from random import randint
# Sao paulo - Daniel
# Sao Bernardo -  Marco
# Rio de Janeiro - Brenno
# Belo Horizonte - luis

file = open("names.txt", "r")
names = file.read()
namesList = names.split("\n")

i = 0
for name in namesList:
    namesList[i] = "\'" + name + "\'"
    i += 1

regionList = [["Sao Paulo", "Sao Paulo", "Brasil"], ["Sao Bernardo do Campo", "Sao Paulo", "Brasil"],
              ["Belo Horizonte", "Minas Gerais", "Brasil"], ["Rio de Janeiro", "Rio de Janeiro", "Brasil"]]


db = mysql.connector.connect(user='root',
                              password='xxxx',
                              host='127.0.0.1',
                              database='ueg')
cursor = db.cursor()

cursor.execute("INSERT INTO tb_pais (Pais) values ('Brasil')")

cursor.execute("INSERT INTO tb_estado (Estado, pais_id) "
               "values ('Sao Paulo', (SELECT pais_id FROM tb_pais WHERE pais = 'Brasil' LIMIT 1))")
cursor.execute("INSERT INTO tb_estado (Estado, pais_id) "
               "values ('Minas Gerais', (SELECT pais_id FROM tb_pais WHERE pais = 'Brasil' LIMIT 1))")
cursor.execute("INSERT INTO tb_estado (Estado, pais_id) "
               "values ('Rio de Janeiro', (SELECT pais_id FROM tb_pais WHERE pais = 'Brasil' LIMIT 1))")
cursor.execute("INSERT INTO tb_estado (Estado, pais_id) "
               "values ('Rio Grande do Sul', (SELECT pais_id FROM tb_pais WHERE pais = 'Brasil' LIMIT 1))")

cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) "
               "values ('Sao Bernardo do Campo', (SELECT estado_id FROM tb_estado WHERE estado = 'Sao Paulo' LIMIT 1))")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) "
               "values ('Belo Horizonte', (SELECT estado_id FROM tb_estado WHERE estado = 'Minas Gerais' LIMIT 1))")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) "
               "values ('Rio de Janeiro', (SELECT estado_id FROM tb_estado WHERE estado = 'Rio de Janeiro' LIMIT 1))")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) "
               "values ('Porto Alegre', (SELECT estado_id FROM tb_estado WHERE estado = 'Rio Grande do Sul' LIMIT 1))")


#insert eleitores

i = 0
j = 352104
namesList = namesList[0:84]

for name in namesList:
    cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
                   " VALUES (" + str(j+i) + " ," + name +", " + str(i%4 + 1) + ", '', false);")
    i += 1

cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (666, 'DARTH VADER', 3, '', 0)")

# NULO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (0, 'NULO', 3, '', 0)")

# BRANCO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (1, 'BRANCO', 3, '', 0)")

# NULO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (2, 'NULO', 3, '', 0)")

# BRANCO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (3, 'BRANCO', 3, '', 0)")

# NULO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (4, 'NULO', 3, '', 0)")

# BRANCO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (5, 'BRANCO', 3, '', 0)")

# NULO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (6, 'NULO', 3, '', 0)")

# BRANCO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (7, 'BRANCO', 3, '', 0)")

# NULO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (8, 'NULO', 3, '', 0)")

# BRANCO
cursor.execute("INSERT INTO tb_eleitor(CPF, Nome, Cidade_id, URL, Votou)"
               "VALUES (9, 'BRANCO', 3, '', 0)")

#insert vereadores
i = 0
j = 0
while j < 16:
    CPF = 352104+i
    cursor.execute("insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos)"
                   " values(" + str(CPF) + "," + str(1002+j) + ", 2," + str(j%4 + 1) + ","+str(j%4 + 1)+", 1, 0);")
    i += 1
    j += 1

#insert prefeitos

k = 0
while k < 8:
    CPF = 352104 + i
    cursor.execute("insert into tb_candidato(CPF, Numero, Cargo_id, Cidade_id, Estado_id, Pais_id, Votos)"
                   " values(" + str(CPF) + "," + str(100002+k) + ", 1," + str(k%4 + 1) + ","+str(k%4 + 1)+", 1, 0);")
    i += 1
    k += 1

#insert governadores

k = 0
while k < 8:
    CPF = 352104 + i
    cursor.execute("insert into tb_candidato(CPF, Numero, Cargo_id, Estado_id, Pais_id, Votos)"
                   " values(" + str(CPF) + "," + str(12+k) + ", 3,"+str(k%4 + 1)+", 1, 0);")
    i += 1
    k += 1

#insert deputados

k = 0
while k < 8:
    CPF = 352104 + i
    cursor.execute("insert into tb_candidato(CPF, Numero, Cargo_id, Estado_id, Pais_id, Votos)"
                   " values(" + str(CPF) + "," + str(102+k) + ", 6,"+str(k%4 + 1)+", 1, 0);")
    i += 1
    k += 1

#insert presidentes

k = 0
while k < 2:
    CPF = 352104 + i
    cursor.execute("insert into tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos)"
                   " values(" + str(CPF) + "," + str(10002+k) + ", 4, 1, 0);")
    i += 1
    k += 1

# insert WhiteCandidate and NullCandidate
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(0, 100000, 1, 1, 0)")
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(1, 100001, 1, 1, 0)")

cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(2, 1000, 2, 1, 0)")
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(3, 1001, 2, 1, 0)")

cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(4, 10, 3, 1, 0)")
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(5, 11, 3, 1, 0)")

cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(6, 10000, 4, 1, 0)")
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(7, 10001, 4, 1, 0)")

cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(8, 100, 6, 1, 0)")
cursor.execute("INSERT INTO tb_candidato(CPF, Numero, Cargo_id, Pais_id, Votos) VALUES(9, 101, 6, 1, 0)")

#insert uevs

cursor.execute("INSERT INTO tb_uev(Usuario, Senha, Cidade_id, Ativo) VALUES('uevSaoPaulo', 'saopaulo1', 1, 1)")
cursor.execute("INSERT INTO tb_uev(Usuario, Senha, Cidade_id, Ativo) VALUES('uevBeloHorizonte', 'belohorizonte1', 2, 1)")
cursor.execute("INSERT INTO tb_uev(Usuario, Senha, Cidade_id, Ativo) VALUES('uevRioDeJaneiro', 'riodejaneiro1', 3, 1)")
cursor.execute("INSERT INTO tb_uev(Usuario, Senha, Cidade_id, Ativo) VALUES('uevPortoAlegre', 'portoalegre1', 4, 1)")

db.commit()
db.close()

