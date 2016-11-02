from Voter import Voter


class Candidate(Voter):
    qntVotesPerRegion = None

    def __init__(self, name, cpf, voted_flag, region, photo_url, number, role, nickname):
        super(Candidate, self).__init__(name, cpf, voted_flag, region, photo_url)
        self.number = number
        self.role = role
        self.nickname = nickname
        self.qntVotesPerRegion = {}
        self.votes = 0

    # TODO add in class diagram
    def setVotesPerRegion(self, region_city, votes):
        self.qntVotesPerRegion[region_city] = votes

    def getTotalVotes(self):
        total = 0
        for region, value in self.qntVotesPerRegion.iteritems():
            total += value
        return total

    # TODO diagram
    def toJSON(self):
        return {'name': self.name,
                'number': self.number,
                'role': self.role,
                'nickname': self.nickname,
                'photoURL': self.photoUrl}
