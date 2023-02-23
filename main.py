class Student():
    def __init__(self, nombre, apellido, carnet, cedula, materias, correo = "", telefono = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.cedula = cedula
        self.materias = materias
        self.correo = correo
        self.telefono = telefono

    def cambiarTelefono(self, telefono):
        self.telefono = telefono
    
    def cambiarCorreo(this, correo):
        this.correo = correo

    def imprimirMaterias(self):
        for materia in self.materias:
            print(materia)

    def imprimirDatosEstudiante(estudiante):
        return "Estudiante: {} {} \nCarnet: {} \nCedula: {} \nCorreo: {} \nTelefono: {}".format(estudiante.nombre, estudiante.apellido, estudiante.carnet, estudiante.cedula, estudiante.correo, estudiante.telefono)


estudiante1 = Student("Stefani", "Perez", 1, 1, ["Algoritmos", "Estructuras de Datos"], "stefani.perez@correo.unimet.edu.ve")

print(estudiante1.imprimirDatosEstudiante())
estudiante1.cambiarCorreo("@")
estudiante1.apellido = "Teran"
print(estudiante1.imprimirDatosEstudiante())
estudiante1.imprimirMaterias()