# router_personal.py

from fastapi import APIRouter

# Inicializa el router
# El 'prefix' es la base de todas las rutas definidas en este archivo.
router = APIRouter(prefix="/yorman_alexis_david_lopez")

# Variable para usar en operaciones
mi_edad = 20
mi_animal_favorito = "PERRO" # Reto 1: Cambia "gato" por el nombre de tu animal favorito (ej: "perro")

# Endpoint: /yorman_alexis_david_lopez/saludo
@router.get("/saludo")
def saludo():
    """Reto 2: Endpoint de saludo personalizado. Cambia el mensaje a algo personal."""
    return {"mensaje": "Hola, soy Yorman Alexis David Lopez todo un puto amo en la programacion!"} # ¡Cambia el mensaje aquí!

# Endpoint: /yorman_alexis_david_lopez/numero_favorito
@router.get("/numero_favorito")
def numero_favorito():
    """Reto 3: Devuelve tu número favorito. Cambia el número 7 por tu favorito."""
    return {"numero": 10} # ¡Cambia el 7 por tu número favorito!

# Endpoint: /yorman_alexis_david_lopez/animal_favorito
@router.get("/animal_favorito")
def animal_favorito():
    """Devuelve tu animal favorito usando la variable mi_animal_favorito."""
    return {"animal": mi_animal_favorito}

# Endpoint: /yorman_alexis_david_lopez/edad_en_5_anos
@router.get("/edad_en_5_anos")
def edad_en_5_anos():
    """Devuelve la edad en 5 años usando la variable mi_edad."""
    return {"edad_futura": mi_edad + 5}

# Endpoint: /yorman_alexis_david_lopez/doble/{numero}
@router.get("/doble/{numero}")
def doble(numero: int):
    """Ejemplo: Endpoint que recibe un número en la ruta y devuelve su doble."""
    return {"doble": numero * 2}

# Endpoint: /yorman_alexis_david_lopez/es_par
@router.get("/es_par")
def es_par(num: int = 0):
    """Ejemplo: Endpoint que recibe un número como query param y dice si es par."""
    # Para usar esto, la URL sería: /yorman_alexis_david_lopez/es_par?num=10
    return {"es_par": num % 2 == 0}
