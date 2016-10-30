class Voter(object):
    """
    ======
    Voter class
    ======
        Attributes:
            name: Name of voter
            cpf: Document (Required)
            photoUrl: Url of face photo of voter (Optional)
            votedFlag: if voter has vote in last election
            regionType: Enum :py:obj: ~UegProject.Model.Types.RegionType`
    """

    def __init__(self, name, cpf, voted_flag, region, photo_url=None):
        self.name = name
        self.cpf = cpf
        self.photoUrl = photo_url
        self.votedFlag = voted_flag
        self.region = region

    # TODO add in Diagram
    def toJSON(self):
        return {'name': self.name,
                'cpf': self.cpf,
                'photoURL': self.photoUrl}
