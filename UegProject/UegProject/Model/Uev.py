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
            active: boolean -> tells if uev is active
    """

    def __init__(self, username, password, region, voters, active):
        self.username = username
        self.password = password
        self.region = region
        self.__voters = voters
        self.__candidates = []
        self.__active = active

    def getVoters(self):
        return self.__voters

    def getCandidates(self):
        return self.__candidates

    def isActive(self):
        return self.__active

    def addCandidate(self, candidate):
        self.__candidates.append(candidate)
