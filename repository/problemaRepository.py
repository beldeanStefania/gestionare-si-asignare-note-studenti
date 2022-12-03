class ProblemaRepository:
    def __init__(self):
        self.__probleme = {}

    def getAll(self):
        """
        returneaza lista de probleme
        :return: o lista de obiecte de tipul Problema
        """
        return list(self.__probleme.values())

    def getById(self, idLab):
        """
        returneaza laboratorul cu id-ul dat
        :param idLab: string
        :return: un obiect de tipul Problema, altfel None
        """
        if idLab in self.__probleme:
            return self.__probleme[idLab]
        return None

    def adauga(self, problema):
        """
        adauga un student in dictionar
        :param problema: obiect de tipul Student
        :return:
        """
        if self.getById(problema.getLab()) is not None:
            raise KeyError("Exista deja studentul cu id-ul dat")
        self.__probleme[problema.getLab()] = problema

    def modifica(self, problemanoua):
        """
        modifica o problema in dictionar
        :param problemanoua: obiect de tipul problema
        :return:
        """
        if self.getById(problemanoua.getLab()) is None:
            raise KeyError("Nu exista problema cu id-ul dat")
        self.__probleme[problemanoua.getLab()] = problemanoua


    def sterge(self, idLab):
        """
        sterge problema cu id-ul dat din dictionar
        :param idLab: string
        :return:
        """
        if self.getById(idLab) is None:
            raise KeyError("Nu exista problema cu id-ul dat")
        self.__probleme.pop(idLab)