import Types.RegiaoType

class Eleitor(object):
    """
        eleitor class
    """

    def __init__(self, nome, cpf, fotourl, fotoobrigatoriaflag, votouflag):
        self.nome = nome
        self.cpf = cpf
        self.fotoURL = fotourl
        self.fotoObrigatoriaFlag = fotoobrigatoriaflag
        self.votouFlag = votouflag
        # self.regiaoVota = RegiaoType

    def set_foto_obrigatoria(self, obrigatorio):
        self.fotoObrigatoriaFlag = obrigatorio

    def is_foto_obrigatoria(self):
        return self.fotoObrigatoriaFlag

