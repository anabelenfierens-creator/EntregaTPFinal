estudiantes ={
    "001" :{"nombre":"Ana", "Edad":"38", "curso":"python"},
    "002" :{"nombre":"Emilio", "Edad":"42", "curso":"Data Scienci"},
    "003" :{"nombre":"Isabel", "Edad":"4", "curso":"Analista de datos"},
    "004" :{"nombre":"Ivan", "Edad":"2", "curso":"Pintura"},
    "005" :{"nombre":"Juan", "Edad":"325", "curso":"Dibujo"},
}
codigo =input("Ingrese el codigo del estudiante: ")
def consultarEstudiante(codigoEstudiante, listaEstudiante):
    if codigoEstudiante in listaEstudiante:
        print(listaEstudiante[codigoEstudiante])
    else:
        print("Estudiante no encontrado")
consultarEstudiante(codigo, estudiantes)