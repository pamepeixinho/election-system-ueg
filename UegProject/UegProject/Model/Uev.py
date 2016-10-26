class Uev(object):
    """
    ======
    Uev class
    ======
        Attributes:
            username
            password
            region
            voters
            candidates
    """

    def __init__(self, username, password, region, voters, candidates):
        self.__username = username
        self.__password = password
        self.__region = region
        self.__voters = voters
        self.__candidates = candidates

    def getVoters(self):
        return self.__voters

    def getCandidates(self):
        return self.__candidates
