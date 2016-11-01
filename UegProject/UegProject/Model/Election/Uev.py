class Uev(object):
    """
    ======
    Uev class
    ======
        Attributes:
            username
            password
            region
            voters
            candidates
            active: boolean -> tells if uev is active
    """
    null_votes = 0
    white_votes = 0

    def __init__(self, username, password, region, voters, candidates, active):
        self.username = username
        self.password = password
        self.region = region
        self.voters = voters
        self.candidates = candidates
        self.active = active

    def isActive(self):
        return self.active
