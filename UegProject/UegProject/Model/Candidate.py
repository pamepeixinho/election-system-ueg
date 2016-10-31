#from UegProject.Model.Voter import Voter
from Voter import Voter


class Candidate(Voter):
    qntVotesPerRegion = None

    def __init__(self, name, cpf, voted_flag, region, photo_url, number, role, nickname):
        super(Candidate, self).__init__(name, cpf, voted_flag, region, photo_url)
        self.number = number
        self.role = role
        self.nickname = nickname
        self.votes = 0

    def toJSON(self):
        return {'name': self.name,
                'number': self.number,
                'role': self.role,
                'nickname': self.nickname,
                'photoURL': self.photoUrl}
