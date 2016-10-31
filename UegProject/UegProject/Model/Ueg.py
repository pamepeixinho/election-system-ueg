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
    # TODO elections variables---
    endElectionToday = None
    nullVotes = None
    whiteVotes = None
    currentUev = None


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
                self.currentUev = uev
                return True
        return False

    def isValidElection(self, communication_type):
        valid_election, self.endElectionToday = self.allElections.validElectionByCommunicationType(communication_type)
        return valid_election

    # TODO finish functions
    def fillVotes(self, votes_voters, votes_candidates, null_votes, white_votes):
        # dataaccess.updatecandidates
        # dataaccess.updatevoters
        return

    def getVotersPerUev(self):
        return self.currentUev.getVoters()

    def getCandidatesPerUev(self):
        return self.currentUev.getCandidates()


    def getAllCandidates(self):
        candidates = []
        for uev in self.uevs:
            candidates.append(uev.getCandidates())
        return candidates

    def getAllVoters(self):
        voters = []
        for uev in self.uevs:
            voters.append(uev.getVoters())
        return voters

    def getAllUevs(self):
        return self.uevs
