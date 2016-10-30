from UegProject.Model.Voter import Voter


class Candidate(Voter):
    """
    ======
    Candidate class
    ======
        Attributes:
            number: number of candidate
            role: Enum :py:obj: ~UegProject.Model.Types.RoleType`
            nickname: nickname of candidate
            regions: regions that candidate is elegible for
            QntVotesPerRegion: Map(Regions, Int)

            - inherited of Voter:
            name: Name of candidate
            cpf: Document (Required)
            photoUrl: Url of face photo of voter (Required)
            votedFlag: if voter has vote in last election
            regionType: Enum :py:obj: ~UegProject.Model.Types.RegionType`
    """

    qntVotesPerRegion = None

    def __init__(self, name, cpf, voted_flag, region, photo_url, number, role, nickname):
        super(Candidate, self).__init__(name, cpf, voted_flag, region, photo_url)
        self.number = number
        self.role = role
        self.nickname = nickname

    def toJSON(self):
        return {'name': self.name,
                'number': self.number,
                'role': self.role,
                'nickname': self.nickname,
                'photoURL': self.photoUrl}
