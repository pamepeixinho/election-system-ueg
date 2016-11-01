import hashlib

from UegProject.Management.Reports import Reports
from UegProject.Model.Election.Candidate import Candidate
from UegProject.Model.Election.Elections import Elections
from UegProject.Model.Election.Region import Region
from UegProject.Model.Election.Uev import Uev
from UegProject.Model.Types.RoleType import RoleType


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
    currentUev = None

    # TODO create constructor -> get all data from DataAccess
    def __init__(self):
        # self.uevs = getList from DataAccess
        # self.allElections = getList from DataAccess
        self.testingUegConstr()

    def testingUegConstr(self):
        self.uevs = [
            Uev("pamela", "1234", Region("regiao1", "sao paulo", "Brasil"), "voters", "candidates", 1),
            Uev("admin", "admin", Region("regiao2", "sao paulo", "Brasil"), "voters", "candidates", 1)
        ]
        self.uevs[0].null_votes = 10
        self.uevs[1].null_votes = 20
        self.uevs[0].white_votes = 20
        self.uevs[1].white_votes = 10
        self.allElections = Elections.testingElectionsModel()

    def Ascertainment(self):
        # Reports.report_total_votes(self.getAllCandidates())
        candidates = Ueg.testingWithCandidatesArray()
        self.testingVotes(candidates)
        null_votes, white_votes = self.getAllNullWhiteVotes()
        Reports.report_total_votes(candidates, null_votes, white_votes)
        Reports.report_uev_votes(candidates)
        Reports.close_pdf()

        return 1

    def getAllNullWhiteVotes(self):
        null_votes = 0
        white_votes = 0

        for uev in self.uevs:
            null_votes += uev.null_votes
            white_votes += uev.white_votes

        return null_votes, white_votes

    def testingVotes(self, candidates):
        for c in (0, 1, 2, 3):
            candidates[c].setVotesPerRegion("Sao Paulo", c+10)
            candidates[c].setVotesPerRegion("Sao Bernardo do Campo", c + 6)
            if c == 0:
                candidates[c].setVotesPerRegion("Sao Joao", 20)

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
        # TODO verify
        # for candidate in self.currentUev.getCandidates():
        # candidate.setVotesPerRegion(self.currentUev.region.city, 100)
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

    @staticmethod
    def testingWithCandidatesArray():
        r = Region("Sao Paulo", "Sao Paulo", "Brasil")
        r2 = Region("Sao Bernardo do Campo", "Sao Paulo", "Brasil")
        vt2 = [Candidate("Darth Vader", 123, False, r, "0.0.0.0:8181/candidate/vader/photo", 102,
                         RoleType.DEPUTADO, "vaderzin"),
               Candidate("Andre", 124, False, r, "url", 103, RoleType.PREFEITO, "dede"),
               Candidate("Ahmad", 125, False, r2, "url", 104, RoleType.PREFEITO, "mud"),
               Candidate("Pamela", 126, False, r, "0.0.0.0:8181/candidate/peixinho/photo", 105,
                         RoleType.GOVERNADOR, "peixinho")
               ]
        return vt2

ueg = Ueg()
ueg.Ascertainment()
