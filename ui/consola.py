from service.problemaService import ProblemaService
from service.studentService import StudentService


class Consola:
    def __init__(self, studentService : StudentService, problemaService : ProblemaService):
        self.__studentService = studentService
        self.__problemaService = problemaService

    def AfisareStudenti(self, studenti):
        for student in studenti:
            print(student)

    def AfisareProbleme(self, probleme):
        for problema in probleme:
            print(problema)

    def AdaugaStudent(self):
        try:
            idStud = input("Scrieti id-ul studentului: ")
            nume = input("Scrieti numele studentului: ")
            grupa = input("Scrieti grupa din care face parte studentul: ")
            idLab = input("Scrieti id-ul laboratorului sau nimic daca studentul nu are asignat un laborator")
            self.__studentService.adauga(idStud, nume, grupa, idLab)
        except KeyError as e:
            print (e)
        except ValueError as e:
            print(e)

    def AdaugaProblema(self):
        idLab = input("Scrieti id-ul laboratorului: ")
        idpb = input("Scrieti id-ul problemei: ")
        descriere = input("Scrieti desctierea problemei: ")
        deadline = input("DEADLINE: ")
        self.__problemaService.adaugaProblema(idLab, idpb, descriere, deadline)

    def ModificaStudent(self):
        try:
            idStud = input("Dati id-ul studentului de modificat: ")
            nume = input("Dati un nume nou: ")
            grupa = input("Dati grupa noua: ")
            idLab = input("Scrieti id-ul noului laborator: ")
            self.__studentService.modifica(idStud, nume, grupa, idLab)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def ModificaProblema(self):
        try:
            idLab = input("Scrieti id-ul laboratorului: ")
            idPb = input("Scrieti noul numar al problemei: ")
            descriere = input("Scrieti noua descriere: ")
            deadline = input("DEADLINE: ")
            self.__problemaService.modificaProblema(idLab, idPb, descriere, deadline)
        except KeyError as e:
            print(e)

    def StergeStudent(self):
        try:
            idStud = input("Dati id-ul studentului de sters: ")
            self.__studentService.stergere(idStud)
        except KeyError as e:
            print(e)

    def StergeProblema(self):
        try:
            idLab = input("Dati id-ul laboratorului de sters: ")
            self.__problemaService.stergeProblema(idLab)
        except KeyError as e:
            print(e)


    def PrintMenu(self):
        print("1. Adauga student")
        print("2. Modifica student")
        print("3. Sterge student")
        print("4. Adauga laboratorul")
        print("5. Modifica laboratorul")
        print("6. Sterge laboratorul")
        print("a. Afiseaza toti studentii")
        print("b. Afiseaza toate problemele")

    def Menu(self):
        while True:
            self.PrintMenu()
            optiune = input("Scrieti optiunea: ")
            if optiune == "1":
                self.AdaugaStudent()
            elif optiune == "2":
                self.ModificaStudent()
            elif optiune == "3":
                self.StergeStudent()
            elif optiune =="4":
                self.AdaugaProblema()
            elif optiune == "5":
                self.ModificaProblema()
            elif optiune == "6":
                self.StergeProblema()
            elif optiune == "a":
                self.AfisareStudenti(self.__studentService.getAllStudenti())
            elif optiune =="b":
                self.AfisareProbleme(self.__problemaService.getAllProbleme())
