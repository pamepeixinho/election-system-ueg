from Voter import Voter


class Candidate(Voter):
    qntVotesPerUev = None

    def __init__(self, name, cpf, voted_flag, region, photo_url, number, role, nickname):
        super(Candidate, self).__init__(name, cpf, voted_flag, region, photo_url)
        self.number = number
        self.role = role
        self.nickname = nickname
        self.qntVotesPerUev = {}
        self.votes = 0

    # TODO add in class diagram
    def setVotesPerUev(self, uev_username, votes):
        self.qntVotesPerUev[uev_username] = votes

    def getTotalVotes(self):
        total = 0
        for region, value in self.qntVotesPerUev.iteritems():
            total += value
        return total

    # TODO diagram and fix IP address
    def toJSON(self):
        return {'name': self.name,
                'number': self.number,
                'role': str(self.role).upper(),
                'nickname': self.nickname if self.nickname is not None else '',
                'photoURL': "192.168.0.1/candidate/{0}/photo".format(
                    self.name) if self.name != "NULO" and self.name != "BRANCO" else ""
                }
