# coding=utf-8
import json

from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from UegProject.ErrorCodes import ErrorCodes
from UegProject.Management.Ueg import Ueg
from UegProject.Model.Election.Candidate import Candidate
from UegProject.Model.Election.Region import Region
from UegProject.Model.Election.Voter import Voter
from UegProject.Model.Types.CommunicationType import CommunicationType as CT
from UegProject.Model.Types.RoleType import RoleType


class Communication(object):
    ueg = None

    def home(self, request):
        self.__verifyIfNew()
        return HttpResponse('UEG')

    def sendData(self, request):
        if request.method != 'GET':
            return HttpResponse(ErrorCodes.WRONG_REQUEST)

        username = request.GET.get('username')
        password = request.GET.get('password')

        self.__verifyIfNew()

        authenticated = self.__authenticate(username, password, CT.CARREGAMENTO)
        if authenticated is not True:
            return HttpResponseForbidden('ERRO {0}'.format(authenticated))

        uev_json = self.__getUevJson()

        return JsonResponse(uev_json, safe=False)

    @csrf_exempt
    def recieveData(self, request):
        """
        curl -H "Content-Type: application/json" -X POST -d '{"username":"pamela", "password":"81dc9bdb52d04dc20036dbd8313ed055", "voters":"v", "candidates":"c", "nullVotes":"null", "whiteVotes":"null"}' 127.0.0.1:8181/results/
        """
        if request.method != 'POST':
            return HttpResponse(ErrorCodes.WRONG_REQUEST)

        json_data = json.loads(request.body, parse_int=int)

        self.__verifyIfNew()

        authenticated = self.__authenticate(json_data["username"], json_data["password"], CT.RECEBIMENTO)
        if authenticated is not True:
            return HttpResponseForbidden('ERRO {0}'.format(authenticated))

        print json_data["voters"][0]["voted"]
        print json_data["whiteVotes"]
        print json_data["nullVotes"]

        self.ueg.fillVotes(json_data["voters"], json_data["candidates"],
                           json_data["nullVotes"], json_data["whiteVotes"])

        return HttpResponse('OK')

    def ascertainment(self, request):
        self.__verifyIfNew()

        filename = self.ueg.ascertainment()

        if filename == u"Erro ao Carregar Apuração, recarregue esse página":
            return HttpResponse(filename)

        with open(filename, "rb") as fid:
            filedata = fid.read()

        #  use this to download pdf
        # response = HttpResponse(filedata, content_type="text/plain")

        response = HttpResponse(filedata, content_type="application/pdf")
        return response

    # TODO add in diagram - fix names
    def candidatePhoto(self, request, candidate_name):
        print candidate_name
        image_path = None
        if candidate_name == "vader":
            image_path = "DarthVader2016"
        elif candidate_name == "peixinho":
            image_path = "dory2016"

        return self._get_image_response("CandidatesImages", image_path)

    def voterPhoto(self, request, voter_name):
        image_path = None
        if voter_name == "yoda":
            image_path = "yoda"

        return self._get_image_response("VotersImages", image_path)

    def __getUevJson(self):
        uev_json = {
            "electionEnd": self.ueg.endElectionToday.isoformat(),
            "voters": [v.toJSON() for v in self.ueg.getVotersPerUev()],
            "candidates": [c.toJSON() for c in self.ueg.getCandidatesPerUev()]
        }
        return uev_json

    def __verifyIfNew(self):
        if self.ueg is None:
            self.ueg = Ueg()

    # TODO verify and update __authenticate usage in diagrams
    def __authenticate(self, username, password, communicationType):
        if self.ueg.isValidUev(username=username, password=password):
            if self.ueg.isValidElection(communicationType):
                return True
            else:
                return ErrorCodes.INVALID_TIME_ELECTION
        else:
            return ErrorCodes.INVALID_UEV

    @staticmethod
    def _get_image_response(folder_path, image_path):
        try:
            with open("UegProject/{0}/{1}.jpg".format(folder_path, image_path), "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            return HttpResponse("null")


    """
    FUNCTIONS JUST FOR TEST \/
    """
    @staticmethod
    def __testingWithVotersArray():
        r = Region("Sao Paulo", "Sao Paulo", "Brasil")
        r2 = Region("Sao Bernardo do Campo", "Sao Paulo", "Brasil")
        vt1 = [Voter("Pamela", 123, False, r),
               Voter("Andre", 124, False, r),
               Voter("Ahmad", 125, False, r2),
               Voter("Marco", 126, False, r)]
        return vt1

    @staticmethod
    def testingWithCandidatesArray():
        r = Region("Sao Paulo", "Sao Paulo", "Brasil")
        r2 = Region("Sao Bernardo do Campo", "Sao Paulo", "Brasil")
        vt2 = [Candidate("Darth Vader", 123, False, r, "0.0.0.0:8181/candidate/vader/photo", 102,
                         RoleType.DEPUTADO, "vaderzin"),
               Candidate("Andre", 124, False, r, "url", 103, RoleType.PREFEITO, "dede"),
               Candidate("Ahmad", 125, False, r2, "url", 104, RoleType.PREFEITO, "mud"),
               Candidate("Pamela", 126, False, r, "0.0.0.0:8181/candidate/peixinho/photo", 105,
                         RoleType.GOVERNADOR, "peixinho")]
        return vt2

