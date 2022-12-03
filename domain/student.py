class Student:
    def __init__(self, idStud, nume, grupa, idLab):
        self.__idStud = idStud
        self.__nume = nume
        self.__grupa = grupa
        self.__idLab = idLab
        #self.__idLab = idLab

    def getIdLab(self):
        return self.__idLab

    def setIdLab(self, idLab):
        self.__idLab = idLab

    def getIdStud(self):
        return self.__idStud

    def getNume(self):
        return self.__nume

    def getGrupa(self):
        return self.__grupa

    def setIdStud(self, idStud):
        self.__idStud = idStud

    def setNume(self, nume):
        self.__nume = nume

    def setGrupa(self, grupa):
        self.__grupa = grupa

    def __str__(self):
        return f" id student: {self.__idStud}, nume: {self.__nume}, grupa: {self.__grupa}, id laborator: {self.__idLab}"


