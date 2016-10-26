import os
import time
import mysql.connector

class DataAccess:

    def __init__(self):
        self._connect_database()

    def _connect_database(self):
        try:
            self.__db = mysql.connector.connect(user='ahmad',
                                                password='1234',
                                                host='127.0.0.1',
                                                database='ueg')
            self.__cursor = self.__db.cursor()

        except:
            print("Unable to connect, verify database status.")
            time.sleep(0.5)
            self._connect_database()


    def getUevList(self):
        self.__cursor.execute("SELECT EL.nome, C.Cidade, E.Estado, P.Pais "
                              "FROM tb_eleitor AS EL "
                              "INNER JOIN tb_cidade AS C ON EL.Cidade_id = C.Cidade_id "
                              "INNER JOIN tb_estado AS E ON C.Estado_id = E.Estado_id "
                              "INNER JOIN tb_pais AS P ON E.Pais_id = P.Pais_id;")
        self.__eleitoresList = self.__cursor.fetchall()
        for x in self.__eleitoresList:
            print(x)

        self.__cursor.execute("SELECT U.Usuario, U.Senha, C.Cidade, E.Estado, P.Pais FROM tb_uev AS U "
                              "INNER JOIN tb_cidade AS C ON C.Cidade_id = U.Cidade_id "
                              "INNER JOIN tb_estado AS E ON C.Estado_id = E.Estado_id "
                              "INNER JOIN tb_pais AS P ON E.Pais_id = P.Pais_id;")
        self.__uevList = self.__cursor.fetchall()
        for x in self.__uevList:
            print(x)

        for uev in self.__uevList:
            for eleitor in self.__eleitoresList:
                if eleitor[1] == uev[2]:
                    print(eleitor[0])
            #print("\n")

    #
    # def setVotesPerCandidate(self, candidates):
    #
    # def setFlagVotesVoter(self, voters):



d = DataAccess()
d.getUevList()