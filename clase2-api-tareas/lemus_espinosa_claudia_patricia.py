from fastapi import APIRouter

router = APIRouter(prefix="/lemus_espinosa_claudia_patricia")

# Variable para usar en operaciones
mi_edad = 37
mi_animal_favorito = "tigre"  # Reto 1: Cambia "gato" por el nombre de tu animal favorito (ej: "perro") 

@router.get("/saludo")
def saludo():
    """Reto 2: Endpoint de saludo personalizado. Cambia el mensaje a algo personal."""
    return {"mensaje": "Hola, estoy aprendiendo a usar FastAPI!"} # muestra un saludo con un mensaje personalizado

@router.get("/numero_favorito")
def numero_favorito():
    """Reto 3: Devuelve tu número favorito. Cambia el número 7 por tu favorito."""
    return {"numero": 28} # muestra tu número favorito

@router.get("/animal_favorito")
def animal_favorito():
    """Devuelve tu animal favorito usando la variable mi_animal_favorito."""
    return {"animal": mi_animal_favorito} # muestra el animal favorito

@router.get("/edad_en_5_anos")
def edad_en_5_anos():
    """Devuelve la edad en 5 años usando la variable mi_edad."""
    return {"edad_futura": mi_edad + 5} # muestra tu edad futura

@router.get("/doble/{numero}")
def doble(numero: int):
    """Ejemplo: Endpoint que recibe un número en la ruta y devuelve su doble."""
    return {"doble": numero * 2} # muestra el doble del número recibido

@router.get("/es_par")
def es_par(num: int = 0):
    """Ejemplo: Endpoint que recibe un número como query param y dice si es par."""
    return {"es_par": num % 2 == 0} # indica si el número es par en el navegador se consulta asi: es_par?num=14

# Desafío 4: Crea un endpoint /suma/{a}/{b} que reciba dos números en la ruta y devuelva su suma
# Para crear este endpoint:
# 1. Usa @router.get("/suma/{a}/{b}")
# 2. La función debe recibir a: int, b: int
# 3. Devuelve {"suma": a + b}
# Ejemplo: /suma/3/4 debería devolver {"suma": 7}
@router.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    """Endpoint que recibe dos números en la ruta y devuelve su suma."""
    return {"suma": a + b}  # muestra la suma de los dos números recibidos  


# Desafío 5: Crea un endpoint /multiplica que reciba dos números como parámetros de query (num1 y num2) y devuelva su producto
# Para crear este endpoint:
# 1. Usa @router.get("/multiplica")
# 2. La función debe recibir num1: int = 0, num2: int = 0
# 3. Devuelve {"producto": num1 * num2}
# Ejemplo: /multiplica?num1=3&num2=4 debería devolver {"producto": 12}
@router.get("/multiplica")
def multiplica(num1: int = 0, num2: int = 0):
    """Endpoint que recibe dos números como query params y devuelve su producto."""
    return {"producto": num1 * num2}  # muestra el producto de los dos números recibidos en el navegador se consulta asi: multiplica?num1=3&num2=4


    
