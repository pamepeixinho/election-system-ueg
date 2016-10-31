import os
import time
import mysql.connector
from Model.Voter import Voter
from Model.Region import Region
from Model.Uev import Uev
from Model.Candidate import Candidate
import abc

class DataAccess:
    __metaclass__ = abc.ABCMeta

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
        self._connect_database()

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
                if candidate[8] == "Presidente":
                    uev.addCandidate(Candidate(candidate[0], candidate[1], candidate[2], Region(candidate[3],
                    candidate[4], candidate[5]), candidate[6], candidate[7], candidate[8], candidate[0]))
                elif candidate[8] == "Deputado" or candidate[8] == "Governador":
                    if candidate[4] == uev.region.state:
                        uev.addCandidate(Candidate(candidate[0], candidate[1], candidate[2], Region(candidate[3],
                        candidate[4], candidate[5]), candidate[6], candidate[7], candidate[8], candidate[0]))
                else:
                    if candidate[3] == uev.region.city:
                        uev.addCandidate(Candidate(candidate[0], candidate[1], candidate[2], Region(candidate[3],
                        candidate[4], candidate[5]), candidate[6], candidate[7], candidate[8], candidate[0]))

        self.__db.close()
        return self.__uevList

    def setVotesPerCandidate(self, candidate):
        self._connect_database()

        queryUpdateVotes = "UPDATE tb_candidato " \
                           "SET Votos = " + str(candidate.votes) + " "\
                           "WHERE CPF = " + str(candidate.cpf) + ";"

        self.__cursor.execute(queryUpdateVotes)
        self.__db.commit()
        self.__db.close()
        print("update")
    #
    # def setFlagVotesVoter(self, voters):

c = Candidate("iLunner", 5, 0, Region("a", "b", "c"), "url", 1, "Prefeito", "sd")
x = 0
while x < 56:
    c.increaseVotes()
    x += 1

DataAccess().setVotesPerCandidate(c)