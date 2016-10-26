import datetime

from UegProject.Model.Election.ElectionDate import ElectionDate
from UegProject.Model.Types.CommunicationType import CommunicationType as CT


class Elections(object):
    """
    ======
    Elections class
    ======
        Attributes:
            electionsList: array list of ElectionDay entity
    """

    def __init__(self, electionList):
        self.__electionsList = electionList

    def typeOfCommunicationByElection(self):

        now = datetime.datetime.now()

        for electionDate in self.__electionsList:
            if electionDate.date == now.date():
                dfstart = datetime.timedelta(hours=electionDate.startTime.hour, minutes=electionDate.startTime.minute,
                                             seconds=0, microseconds=0)
                dfend = datetime.timedelta(hours=electionDate.stopTime.hour, minutes=electionDate.stopTime.minute,
                                           seconds=0, microseconds=0)

                dfnow = datetime.timedelta(hours=now.hour, minutes=now.minute, seconds=0, microseconds=0)

                if abs(dfnow - dfstart) < abs(dfnow - dfend):
                    return CT.CARREGAMENTO
                else:
                    return CT.RECEBIMENTO


#Just for testing
def testingModel():

    d0 = ElectionDate(2016, 10, 26, 8, 0, 18, 0)
    d1 = ElectionDate(2016, 10, 27, 8, 0, 18, 0)
    d2 = ElectionDate(2016, 10, 25, 8, 0, 18, 0)
    d3 = ElectionDate(2016, 10, 24, 8, 0, 18, 0)

    list = [d0, d1, d2, d3]

    elections = Elections(list)

    print elections.typeOfCommunicationByElection()


testingModel()
