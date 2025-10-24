from fastapi import APIRouter

router = APIRouter(prefix="/evelyn_tatiana_rojas_gutierrez")

# Variable para usar en operaciones
mi_edad = 28
mi_animal_favorito = "perro"  # Reto 1: Cambia "gato" por el nombre de tu animal favorito ( "perro")

@router.get("/saludo")
def saludo():
    """Reto 2: Endpoint de saludo personalizado. Cambia el mensaje a algo personal."amo a mis hijos"""
    return {"mensaje": "Hola, soy Evelyn Tatiana Rojas Gutierrez, la tralalerita superior, dueña de todos los tralaleros del mundo"}

@router.get("/numero_favorito")
def numero_favorito():
    """Reto 3: Devuelve tu número favorito. Cambia el número 7 por tu favorito."""
    return {"numero":4}

@router.get("/animal_favorito")
def animal_favorito():
    """Devuelve tu animal favorito usando la variable mi_animal_favorito."""
    return {"animal": mi_animal_favorito}

@router.get("/edad_en_5_anos")
def edad_en_5_anos():
    """Devuelve la edad en 5 años usando la variable mi_edad."""
    return {"edad_futura": mi_edad + 3 }

@router.get("/doble/{numero}")
def doble(numero: int):
    """Ejemplo: Endpoint que recibe un número en la ruta y devuelve su doble."""
    return {"doble": numero * 4}

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
@router.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    # Este endpoint recibe dos números por la ruta y devuelve su suma
    resultado = a + b
    return {"a": a, "b": b, "resultado": resultado}

# Desafío 5: Crea un endpoint /multiplica que reciba dos números como parámetros de query (num1 y num2) y devuelva su producto
# Para crear este endpoint:
# 1. Usa @router.get("/multiplica")
# 2. La función debe recibir num1: int = 0, num2: int = 0
# 3. Devuelve {"producto": num1 * num2}
# Ejemplo: /multiplica?num1=3&num2=4 debería devolver {"producto": 12}
@router.get("/multiplica/{a}/{b}")
def multiplica(a: int, b: int):
    # Este endpoint recibe dos números como parámetros de consulta (query) y devuelve su multiplicación
    resultado = a * b
    return {"a": a, "b": b, "resultado": resultado}