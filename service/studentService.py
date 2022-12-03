from domain.student import Student
from repository.problemaRepository import ProblemaRepository
from repository.studentRepository import StudentRepository


class StudentService:
    def __init__(self, studentRepository : StudentRepository, problemaRepository : ProblemaRepository):
        self.__studentRepository = studentRepository
        self.__problemaRepository = problemaRepository

    def getAllStudenti(self):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        """
        return self.__studentRepository.getAll()

    def adauga(self, idStud, nume, grupa, idLab):
        """
        adauga un obiect de tipul Student in lista
        :param IdStud: string
        :param nume: string
        :param grupa: string
        :param idLab: string
        :return:
        """
        if idLab !="" and self.__problemaRepository.getById(idLab) is None:
            raise ValueError("Nu exista niciun laborator cu id-ul dat")
        student = Student(idStud, nume, grupa, idLab)
        self.__studentRepository.adauga(student)

    def modifica(self, idStud, nume, grupa, idLab):
        """
        modifica un obiect de tipul Student in lista
        :param idStud: string
        :param nume: string
        :param grupa: string
        :return:
        """
        if idLab !="" and self.__problemaRepository.getById(idLab) is None:
            raise ValueError("Nu exista niciun laborator cu id-ul dat")
        student = Student(idStud, nume, grupa, idLab)
        self.__studentRepository.modifica(student)

    def stergere(self, idStud):
        """
        sterge un obiect de tipul Student
        :param idStud: string
        :return:
        """
        self.__studentRepository.sterge(idStud)


