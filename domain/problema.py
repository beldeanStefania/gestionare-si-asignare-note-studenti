class Problema:
    def __init__(self, nrLab, nrProb , descriere, deadline):
        self.__lab = (nrLab, nrProb)
        self.__descriere = descriere
        self.__deadline = deadline

    def getLab(self):
        return self.__lab[0]

    def setLab(self, nrLab):
        self.__lab[0] = nrLab

    def getLsiP(self):
        return self.__lab

    def getDescriere(self):
        return self.__descriere

    def getDeadline(self):
        return self.__deadline

    def setLsiP(self, nrlab, nrProb):
        self.__lab = (nrlab, nrProb)

    def setDescriere(self, descriere):
        self.__descriere = descriere

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f" nr lab: {self.__lab[0]}, nr pb: {self.__lab[1]}, descriere: {self.__descriere}, deadline: {self.__deadline}"
