class StudentRepository:
    def __init__(self):
        self.__studenti = {}

    def getAll(self):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        """
        return list(self.__studenti.values())

    def getById(self, idStudent):
        """
        returneaza angajatul cu id-ul dat
        :param idStudent: string
        :return: un obiect de tipul Student, altfel None
        """
        if idStudent in self.__studenti:
            return self.__studenti[idStudent]
        return None

    def adauga(self, student):
        """
        adauga un student in dictionar
        :param student: obiect de tipul Student
        :return:
        """
        if self.getById(student.getIdStud()) is not None:
            raise KeyError("Exista deja studentul cu id-ul dat")
        self.__studenti[student.getIdStud()] = student

    def modifica(self, studentnou):
        """
        modifica un student in dictionar
        :param studentnou: obiect de tipul student
        :return:
        """
        if self.getById(studentnou.getIdStud()) is None:
            raise KeyError("Nu exista studentul cu id-ul dat")
        self.__studenti[studentnou.getIdStud()] = studentnou


    def sterge(self, idStudent):
        """
        sterge studentul cu id-ul dat din dictionar
        :param idStudent: string
        :return:
        """
        if self.getById(idStudent) is None:
            raise KeyError("Nu exista studentul cu id-ul dat")
        self.__studenti.pop(idStudent)