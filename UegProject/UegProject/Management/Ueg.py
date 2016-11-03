import hashlib

import numpy as np

from Reports import Reports
from UegProject.DataAccess import DataAccess
from UegProject.Model.Election.Candidate import Candidate
from UegProject.Model.Election.Elections import Elections
from UegProject.Model.Election.Region import Region
from UegProject.Model.Election.Uev import Uev
from UegProject.Model.Election.Voter import Voter
from UegProject.Model.Types.RoleType import RoleType


class Ueg(object):
    """
    ======
    Uev class
    ======
        Attributes:
            Uevs: list of all uevs
            AllElections: Elections
            -
            endElectionToday
            currentUev
    """

    uevs = None
    allElections = None
    endElectionToday = None
    currentUev = None

    # TODO create constructor -> get all data from DataAccess
    def __init__(self):
        self.uevs = DataAccess.getUevList()
        self.allElections = Elections.testingElectionsModel()
        # self.testingUegConstr()

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

    def fillVotes(self, votes_voters, votes_candidates, null_votes, white_votes):

        print votes_voters
        print votes_candidates

        self.setFlagVotesVotersLocal(votes_voters)
        DataAccess.setFlagVotesVoter(self.getAllVoters())

        self.setVotesPerCandidateLocal(votes_candidates)
        DataAccess.setVotesPerCandidate(self.getAllCandidates())

        self.setVotesUevLocal(null_votes, white_votes)
        # TODO data access update null and white votes

    def setFlagVotesVotersLocal(self, votes_voters):
        for i, x in enumerate(votes_voters):
            voter = self.getVoterByCPF(votes_voters[i]["cpf"])
            voter.votedFlag = votes_voters[i]["voted"]

    def getVoterByCPF(self, cpf):
        for voter in self.getAllVoters():
            if voter.cpf == cpf:
                return voter

    def getUevByUsername(self, username):
        for uev in self.uevs:
            if uev.username == username:
                return uev

    def setVotesPerCandidateLocal(self, votes_candidates):
        for i, x in enumerate(votes_candidates):
            candidate = self.getCandidateByNumber(votes_candidates[i]["number"])
            votes = votes_candidates[i]["votes"]
            candidate.votes += votes
            candidate.setVotesPerUev(self.currentUev.username, votes)

    def getCandidateByNumber(self, number):
        for candidate in self.getAllCandidates():
            if candidate.number == number:
                return candidate

    def setVotesUevLocal(self, null_votes, white_votes):
        uev = self.getUevByUsername(self.currentUev.username)
        uev.null_votes = null_votes
        uev.white_votes = white_votes

    def ascertainment(self):
        global filename
        candidates = self.getAllCandidates()
        voters = self.getAllVoters()

        # just for testing
        # self.testingVotes(candidates)
        if len(candidates) != 0 and len(voters) != 0:
            Reports.initPdf()
            null_votes, white_votes = self.getAllNullWhiteVotes()
            Reports.report_total_votes(candidates, null_votes, white_votes)
            Reports.report_uev_votes(candidates, self.uevs, null_votes, white_votes)
            Reports.report_no_show_voter(voters)
            filename = Reports.close_pdf()

        return filename

    def getVotersPerUev(self):
        return self.currentUev.getVoters()

    def getCandidatesPerUev(self):
        return self.currentUev.getCandidates()

    def getAllCandidates(self):
        candidates = []
        for uev in self.uevs:
            candidates += uev.getCandidates()
        return candidates

    def getAllVoters(self):
        voters = []
        for uev in self.uevs:
            voters += uev.getVoters()
        return voters

    def getAllUevs(self):
        return self.uevs

    def getAllNullWhiteVotes(self):
        null_votes = 0
        white_votes = 0

        for uev in self.uevs:
            null_votes += uev.null_votes
            white_votes += uev.white_votes

        return null_votes, white_votes

    def testingVotes(self, candidates):
        for c in np.arange(len(candidates)):
            candidates[c].setVotesPerUev("Sao Paulo", c + 10)
            candidates[c].setVotesPerUev("Sao Bernardo do Campo", c + 6)
            if c == 0:
                candidates[c].setVotesPerUev("Sao Joao", 20)

    def testingUegConstr(self):
        self.uevs = [
            Uev("pamela", "1234", Region("Sao Paulo", "sao paulo", "Brasil"), self.testingWithVotersArray(), 1),
            Uev("admin", "admin", Region("Sao Bernardo do Campo", "sao paulo", "Brasil"),
                self.testingWithVotersArray(),1)
        ]
        for c in self.testingWithCandidatesArray():
            self.uevs[0].addCandidate(c)
            self.uevs[1].addCandidate(c)
            
        self.uevs[0].null_votes = 10
        self.uevs[1].null_votes = 20
        self.uevs[0].white_votes = 20
        self.uevs[1].white_votes = 10
        self.allElections = Elections.testingElectionsModel()

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


    @staticmethod
    def testingWithVotersArray():
        r = Region("Sao Paulo", "Sao Paulo", "Brasil")
        r2 = Region("Sao Bernardo do Campo", "Sao Paulo", "Brasil")
        vt1 = [Voter("Pamela", 123, True, r),
               Voter("Andre", 124, True, r),
               Voter("Ahmad", 125, False, r2),
               Voter("Marco", 126, False, r)]
        return vt1
