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
            -
            null_votes: null votes in this UEV
            white_votes: null votes in this UEV
    """

    null_votes = 0
    white_votes = 0

    def __init__(self, username, password, region, voters, candidates, active):
        self.username = username
        self.password = password
        self.region = region
        self.__voters = voters
        self.__candidates = candidates
        self.__active = active

    def getVoters(self):
        return self.__voters

    def getCandidates(self):
        return self.__candidates

    def isActive(self):
        return self.__active
