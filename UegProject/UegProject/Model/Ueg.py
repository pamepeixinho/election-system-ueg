from UegProject.Model.Election.Elections import Elections
from UegProject.Model.Uev import Uev

import hashlib

class Ueg(object):
    """
    ======
    Uev class
    ======
        Attributes:
            Uevs: list of all uevs
            AllElections: Elections
    """

    uevs = None
    allElections = None

    # TODO create constructor -> get all data from DataAccess
    def __init__(self):
        # self.uevs = getList from DataAccess
        # self.allElections = getList from DataAccess
        self.uevs = [
            Uev("pamela", "1234", "regiao", "voters", "candidates", 1),
            Uev("admin", "admin", "regiao", "voters", "candidates", 1)
        ]
        self.allElections = Elections.testingElectionsModel()

    def Ascertainment(self):
        return 1

    # TODO hash login passowrd MD5
    def isValidUev(self, username, password):
        for uev in self.uevs:
            hash_password = hashlib.md5(uev.password).hexdigest()
            if uev.username == username and hash_password == password and uev.isActive():
                return True
        return False

    def isValidElection(self, communicationType):
        return self.allElections.isValidElectionByCommunicationType(communicationType)

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
