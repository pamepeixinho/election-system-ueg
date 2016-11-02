import mysql.connector

#Sao paulo - Daniel
#Sao Bernardo -  Marco
#Rio de Janeiro - Brenno
#Belo Horizonte - luis

file = open("names.txt", "r")
names = file.read()
namesList = names.split("\n")

i = 0
for name in namesList:
    namesList[i] = "\'" + name + "\'"
    i += 1

regionList = [["Sao Paulo", "Sao Paulo", "Brasil"], ["Sao Bernardo do Campo", "Sao Paulo", "Brasil"],
              ["Belo Horizonte", "Minas Gerais", "Brasil"], ["Rio de Janeiro", "Rio de Janeiro", "Brasil"]]


db =  mysql.connector.connect(user='ahmad',
                              password='1234',
                              host='127.0.0.1',
                              database='ueg')
cursor = db.cursor()

cursor.execute("INSERT INTO tb_pais (Pais) values ('Brasil')")

cursor.execute("INSERT INTO tb_estado (Estado, pais_id) values ('Sao Paulo', 1)")
cursor.execute("INSERT INTO tb_estado (Estado, pais_id) values ('Minas Gerais', 1)")
cursor.execute("INSERT INTO tb_estado (Estado, pais_id) values ('Rio de Janeiro', 1)")

cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) values ('Sao Bernardo do Campo', 1)")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) values ('Sao Paulo', 1)")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) values ('Belo Horizonte', 2)")
cursor.execute("INSERT INTO tb_cidade (Cidade, estado_id) values ('Parati', 3)")

for name in namesList:
    print(name)


