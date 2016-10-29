
from Voter import Voter


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

    qntVotesPerRegion = -1

    def __init__(self, name, cpf, voted_flag, region, photo_url, number, role, nickname):
        super.__init__(self, name, cpf, voted_flag, region, photo_url)
        self.__number = number
        self.__role = role
        self.__nickname = nickname
