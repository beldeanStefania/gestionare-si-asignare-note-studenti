from domain.student import Student
from repository.problemaRepository import ProblemaRepository
from repository.studentRepository import StudentRepository
from service.problemaService import ProblemaService
from service.studentService import StudentService
from ui.consola import Consola


def main():
    studentRepository = StudentRepository()
    problemaRepository = ProblemaRepository()
    studentService = StudentService(studentRepository, problemaRepository)
    problemaService = ProblemaService(problemaRepository, studentRepository)
    consola = Consola(studentService, problemaService)

    consola.Menu()

main()
