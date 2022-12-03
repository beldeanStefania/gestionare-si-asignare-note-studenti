from domain.problema import Problema
from domain.student import Student


class Asignare:
    def __init__(self, student: Student, problema: Problema):
        self.__student = student
        self.__problema = problema

    def getStudent(self):
        return self.__student

    def getProblema(self):
        return self.__problema

    def setStudent(self, student: Student):
        self.__student.setNume(student.getNume())
        self.__student.setGrupa(student.getGrupa())
        self.__student.setIdStud(student.getIdStud())

    def setProblema(self, problema: Problema):
        self.__problema.setLab(problema.getLab())
        self.__problema.setDescriere(problema.getDescriere())
        self.__problema.setDeadline(problema.getDeadline())