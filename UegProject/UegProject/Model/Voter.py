from numpy.distutils.fcompiler import none


class Voter(object):
    """
    ======
    eleitor class
    ======
        Attributes:
            name: Name of voter
            cpf: Document (Required)
            photoUrl: Url of face photo of voter (Optional)
            votedFlag: if voter has vote in last election
            regionType: Enum :py:obj: ~UegProject.Model.Types.RegionType`
            requiredPhotoFlag: if required photo -> true
    """

    def __init__(self, name, cpf, voted_flag, region_type, photo_url=none, required_photo_flag=False):
        self.__name = name
        self.__cpf = cpf
        self.__photoUrl = photo_url
        self.__votedFlag = voted_flag
        self.__regionType = region_type
        self.__requiredPhotoFlag = required_photo_flag


    def setrequiredphoto(self):
        self.__requiredPhotoFlag = True


    # MANLY PYTHON WAY OF GETTER AND SETTER ->
    # http://www.python-course.eu/python3_properties.php
    # http: // stupidpythonideas.blogspot.com.br / 2015 / 01 / why - dont - you - want - getters - and -setters.html
    @property
    def cpf(self):
        """I'm the 'required_photo' property."""
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        print "setter of x called"
        self.__cpf = value
