class Persona:
    def __init__(self, nombre, apellido, cedula, correo = "", telefono = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono

    def imprimirDatos(this):
        print("Persona: {} {} \nCedula: {} \nCorreo: {} \nTelefono: {}".format(this.nombre, this.apellido, this.cedula, this.correo, this.telefono))

class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, correo = "", telefono = "", carnet = 0, materias = []):
        super().__init__(nombre, apellido, cedula, correo, telefono)
        self.carnet = carnet
        self.materias = materias

    def imprimirDatos(this):
        print("Carnet: {} \nMaterias: {}".format(this.carnet, this.materias))
        
    def imprimirDatos2(this):
        Persona.imprimirDatos(this)

estudiante1 = Estudiante("Stefani", "Perez", 1, "stefani.perez@correo.unimet.edu.ve", "0424-........", 1, ["Algoritmos", "Estructuras de Datos"])
estudiante1.imprimirDatos2()