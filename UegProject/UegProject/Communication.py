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

    @staticmethod
    def home(request):
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

    def ascertainment(self, request):
    # response file pdf by path
        self.__verifyIfNew()
        self.ueg.testingVotes(self.ueg.getAllCandidates())
        filename = self.ueg.ascertainment()
        # TODO fix response
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        return response


    @csrf_exempt
    def recieveData(self, request):
        """
        curl -H "Content-Type: application/json" -X POST -d '{"username":"pamela","password":"81dc9bdb52d04dc20036dbd8313ed055", "voters":"v", "candidates":"c", "nullVotes":"null", "whiteVotes":"null"}' 127.0.0.1:8181/results/
        """
        if request.method != 'POST':
            return HttpResponse(ErrorCodes.WRONG_REQUEST)
        json_data = json.loads(request.body)

        self.__verifyIfNew()

        authenticated = self.__authenticate(json_data["username"], json_data["password"], CT.RECEBIMENTO)
        if authenticated is not True:
            return HttpResponseForbidden('ERRO {0}'.format(authenticated))

        self.ueg.fillVotes(json_data["voters"], json_data["candidates"],
                           json_data["nullVotes"], json_data["whiteVotes"])

        return HttpResponse('OK')

    def __getUevJson(self):
        uev_json = {
            "electionEnd": self.ueg.endElectionToday.time(),

            # TODO get array BY UEG -----------
            # "Eleitores": [v.toJSON() for v in self.ueg.getVotersPerUev()]
            # "Candidatos": [c.toJSON() for c in self.ueg.getCandidatesPerUev()]
            # TODO ----------------------------

            "voters": [v.toJSON() for v in self.__testingWithVotersArray()],
            "candidates": [c.toJSON() for c in self.testingWithCandidatesArray()],
        }
        return uev_json

    # TODO verify requirement of this function and usage (Diagrams TOO)
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

    @staticmethod
    def _get_image_response(folder_path, image_path):
        try:
            with open("UegProject/{0}/{1}.jpg".format(folder_path, image_path), "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            return HttpResponse("null")

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
