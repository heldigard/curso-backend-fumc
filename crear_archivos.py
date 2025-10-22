import os

estudiantes = [
    "Andrey Perez Blandon",
    "Camila Acevedo Machado",
    "Camilo Andres Riascos Moran",
    "Carlos David Muñoz Galeano",
    "Carlos Felipe Campillo Gómez",
    "Carolina Reina Pineda",
    "Cindy Vanesa Castro Gomez",
    "Cristhian Alexis Gallón Monsalve",
    "Cristian Fernando Ricaurte Estrada",
    "Dacier Dacier Escobar Chima",
    "Daniel Felipe Guerra Rivera",
    "David Yusti Serna",
    "Edison Jaramillo Monsalve",
    "Edwin Alejandro Manrique Rojas",
    "Esteban Ortiz Medina",
    "Evelyn Tatiana Rojas Gutierrez",
    "Henry Mateo Castaño Arias",
    "James Andres Estrada Diosa",
    "Jhon Esteban Quintero Alzate",
    "Jhon Fredy Mena Miranda",
    "Jimmy Alexander Correa",
    "John Fabir Garrido Arenas",
    "Jose Alexis Arango Hernandez",
    "Josmar Enrique Velasquez Urbina",
    "Juan Camilo Ruiz Hoyos",
    "Juan Carlos Arango Sarmiento",
    "Juan David Vega Zapata",
    "Katherin Julieth Henao Pérez",
    "Leidy Viviana Gomez Roman",
    "Lemus Espinosa Claudia Patricia",
    "Liceth Katherine Cano Velasquez",
    "Liliana Maria Garcia Ra Mirez",
    "Luis Felipe Zea Minota",
    "Madelin Ruiz Mejía",
    "Maria Angelica Bermudez Gutierrez",
    "Maria Camila Mona Henao",
    "Mariana Marin Ramirez",
    "Mateo Mejía Mejía",
    "Mayherlyn Lyset Salazar Echavarria",
    "Ronald Vasquez Losada",
    "Salomé Alzate",
    "Sara Jurado Giraldo",
    "Sebastián Giraldo Meza",
    "Sebastian Londoño Vélez",
    "Shirley Tatiana Torres Silva",
    "Sthefanny Gomez Jerez",
    "Ubaldo Jose Meneses Pacheco",
    "Weiner Andres Valencia",
    "Xiomara Xiomara Giraldo Ocampo",
    "Yeniffer Elena Acosta Acosta",
    "Yorman Alexis David Lopez",
    "Yuliana Andrea Perez Tabares",
    "Yuliana Melissa Muñoz Diosa",
    "Yurany Alejandra Garcia Salazar"
]

for estudiante in estudiantes:
    nombre_archivo = estudiante.lower().replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n") + ".py"
    nombre_sin_espacios = estudiante.lower().replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    contenido = '''from fastapi import APIRouter

router = APIRouter(prefix="/''' + nombre_sin_espacios + '''")

# Variable para usar en operaciones
mi_edad = 20
mi_animal_favorito = "gato"  # Reto 1: Cambia "gato" por el nombre de tu animal favorito (ej: "perro")

@router.get("/saludo")
def saludo():
    """Reto 2: Endpoint de saludo personalizado. Cambia el mensaje a algo personal."""
    return {"mensaje": "Hola, soy ''' + estudiante + '''"}

@router.get("/numero_favorito")
def numero_favorito():
    """Reto 3: Devuelve tu número favorito. Cambia el número 7 por tu favorito."""
    return {"numero": 7}

@router.get("/animal_favorito")
def animal_favorito():
    """Devuelve tu animal favorito usando la variable mi_animal_favorito."""
    return {"animal": mi_animal_favorito}

@router.get("/edad_en_5_anos")
def edad_en_5_anos():
    """Devuelve la edad en 5 años usando la variable mi_edad."""
    return {"edad_futura": mi_edad + 5}

@router.get("/doble/{numero}")
def doble(numero: int):
    """Ejemplo: Endpoint que recibe un número en la ruta y devuelve su doble."""
    return {"doble": numero * 2}

@router.get("/es_par")
def es_par(num: int = 0):
    """Ejemplo: Endpoint que recibe un número como query param y dice si es par."""
    return {"es_par": num % 2 == 0}

# Desafío 4: Crea un endpoint /suma/{a}/{b} que reciba dos números en la ruta y devuelva su suma
# Para crear este endpoint:
# 1. Usa @router.get("/suma/{a}/{b}")
# 2. La función debe recibir a: int, b: int
# 3. Devuelve {"suma": a + b}
# Ejemplo: /suma/3/4 debería devolver {"suma": 7}

# Desafío 5: Crea un endpoint /multiplica que reciba dos números como parámetros de query (num1 y num2) y devuelva su producto
# Para crear este endpoint:
# 1. Usa @router.get("/multiplica")
# 2. La función debe recibir num1: int = 0, num2: int = 0
# 3. Devuelve {"producto": num1 * num2}
# Ejemplo: /multiplica?num1=3&num2=4 debería devolver {"producto": 12}
'''
    with open(os.path.join("clase2-api-tareas", nombre_archivo), "w", encoding="utf-8") as f:
        f.write(contenido)

print("Archivos creados.")
