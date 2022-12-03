from domain.problema import Problema
from repository.problemaRepository import ProblemaRepository
from repository.studentRepository import StudentRepository


class ProblemaService:
    def __init__(self, problemaRepository : ProblemaRepository, studentRepository :StudentRepository):
        self.__problemaRepository = problemaRepository
        self.__studentRepository = studentRepository

    def getAllProbleme(self):
        """
        returneaza lista de probleme
        :return: o lista de obiecte de tipul Problema
        """
        return self.__problemaRepository.getAll()

    def adaugaProblema(self, idLab, idPb, descriere, deadline):
        """

        :param idLab:
        :param idPb:
        :param descriere:
        :param deadline:
        :return:
        """
        problema = Problema(idLab, idPb, descriere, deadline)
        self.__problemaRepository.adauga(problema)

    def modificaProblema(self, idLab, idPb, descriere, deadline):
        """

        :param idLab:
        :param idPb:
        :param descriere:
        :param deadline:
        :return:
        """
        problema = Problema(idLab, idPb, descriere, deadline)
        self.__problemaRepository.modifica(problema)

    def stergeProblema(self, idlab):
        """

        :param idlab:
        :return:
        """
        studenti = self.__studentRepository.getAll()
        for student in studenti:
            if student.getIdLab() == idlab:
                self.__studentRepository.sterge(student.getIdStud())
        self.__problemaRepository.sterge(idlab)
