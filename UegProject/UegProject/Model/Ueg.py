from numpy.distutils.fcompiler import none


class Ueg(object):
    """
    ======
    Uev class
    ======
        Attributes:
            Uevs: list of all uevs
            AllElections: Elections
    """

    uevs = none
    allElections = none

    # TODO create constructor
    # def __init__(self):
        # self.uevs = getList from DataAccess
        # self.allElections = getList from DataAccess

    def Ascertainment(self):
        return

    def isValidUev(self, username, password):
        for uev in self.uevs:
            if uev.username == username and uev.password == password and uev.isActive():
                return True
        return False

    def isValidElection(self):
        return self.allElections.typeOfCommunicationByElection()

    # TODO finish functions
    def fillVotes(self):
        return

    def getVotesPerUev(self):
        return

    def getCandidatesPerUev(self):
        return

    def getAllCandidates(self):
        return

    def getAllVoters(self):
        return

    def getAllUevs(self):
        return