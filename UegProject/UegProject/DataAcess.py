import os
import time
import mysql.connector
from Model.Voter import Voter
from Model.Region import Region
from Model.Uev import Uev
from Model.Candidate import Candidate

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
        queryVoters = "SELECT EL.nome, EL.cpf, EL.URL, C.Cidade, E.Estado, P.Pais " \
                      "FROM tb_eleitor AS EL " \
                      "INNER JOIN tb_cidade AS C ON EL.Cidade_id = C.Cidade_id " \
                      "INNER JOIN tb_estado AS E ON C.Estado_id = E.Estado_id " \
                      "INNER JOIN tb_pais AS P ON E.Pais_id = P.Pais_id;"

        queryUevs = "SELECT U.Usuario, U.Senha, C.Cidade, E.Estado, P.Pais, U.Ativo " \
                    "FROM tb_uev AS U " \
                    "INNER JOIN tb_cidade AS C ON C.Cidade_id = U.Cidade_id " \
                    "INNER JOIN tb_estado AS E ON C.Estado_id = E.Estado_id " \
                    "INNER JOIN tb_pais AS P ON E.Pais_id = P.Pais_id;"

        queryCandidates = "SELECT EL.Nome, CA.CPF, EL.Votou, C.Cidade, E.Estado, P.Pais, EL.URL, CA.numero, CAR.Cargo "\
                          "FROM tb_candidato AS CA "\
                          "INNER JOIN tb_eleitor AS EL ON CA.CPF = EL.CPF " \
                          "LEFT JOIN tb_cidade AS C ON CA.Cidade_id = C.Cidade_id " \
                          "LEFT JOIN tb_estado AS E ON CA.Estado_id = E.Estado_id " \
                          "LEFT JOIN tb_pais AS P ON CA.Pais_id = P.Pais_id " \
                          "INNER JOIN tb_cargo AS CAR ON CA.Cargo_id = CAR.cargo_id;"

        self.__cursor.execute(queryVoters)
        self.__eleitoresListDB = self.__cursor.fetchall()

        self.__cursor.execute(queryUevs)
        self.__uevListDB = self.__cursor.fetchall()

        self.__cursor.execute(queryCandidates)
        self.__candidateListDB = self.__cursor.fetchall()

        self.__uevList = []
        for uev in self.__uevListDB:
            self.__voterList = []
            for eleitor in self.__eleitoresListDB:
                if eleitor[3] == uev[2]:
                    self.__voterList.append(Voter(eleitor[0], eleitor[1], 0, Region(eleitor[3],
                    eleitor[4], eleitor[5]), eleitor[2]))
            self.__uevList.append(Uev(uev[0], uev[1], Region(uev[2], uev[3], uev[4]), self.__voterList, uev[5]))

        for uev in self.__uevList:
            for candidate in self.__candidateListDB:
                if(candidate[8] == "Presidente"):
                    uev.addCandidate(Candidate())

    #
    # def setVotesPerCandidate(self, candidates):
    #
    # def setFlagVotesVoter(self, voters):



d = DataAccess()
d.getUevList()