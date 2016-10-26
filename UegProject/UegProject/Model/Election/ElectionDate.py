import datetime


class ElectionDate(object):
    """
    ======
    ElectionDay class
    ======
        Attributes:
            date: date of election
            startTime: starttime of election
            stopTime: end time of election
    """

    def __init__(self, year, month, day, startHour, startMin, stopHour, stopMin):
        self.date = datetime.date(year, month, day)
        self.startTime = datetime.time(startHour, startMin, 0, 0)
        self.stopTime = datetime.time(stopHour, stopMin, 0, 0)
