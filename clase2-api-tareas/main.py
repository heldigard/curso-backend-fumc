from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Tareas - Clase 2",
    description="API REST con operaciones CRUD creada en el curso Backend FUMC",
    version="1.0.0"
)

# Ruta raíz - Endpoint de bienvenida
@app.get("/")
async def root():
    return {
        "mensaje": "¡Bienvenido a la API de Tareas! 2025",
        "version": "1.0.0",
        "endpoints": ["/docs", "/tareas"]
    }

# Endpoint de prueba con parámetro
@app.get("/saludar/{nombre}")
async def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}! Esta API gestiona tareas."}

# Routers de estudiantes
from .andrey_perez_blandon import router as andrey_perez_blandon_router
from .camila_acevedo_machado import router as camila_acevedo_machado_router
from .camilo_andres_riascos_moran import router as camilo_andres_riascos_moran_router
from .carlos_david_munoz_galeano import router as carlos_david_munoz_galeano_router
from .carlos_felipe_campillo_gomez import router as carlos_felipe_campillo_gomez_router
from .carolina_reina_pineda import router as carolina_reina_pineda_router
from .cindy_vanesa_castro_gomez import router as cindy_vanesa_castro_gomez_router
from .cristhian_alexis_gallon_monsalve import router as cristhian_alexis_gallon_monsalve_router
from .cristian_fernando_ricaurte_estrada import router as cristian_fernando_ricaurte_estrada_router
from .dacier_dacier_escobar_chima import router as dacier_dacier_escobar_chima_router
from .daniel_felipe_guerra_rivera import router as daniel_felipe_guerra_rivera_router
from .david_yusti_serna import router as david_yusti_serna_router
from .edison_jaramillo_monsalve import router as edison_jaramillo_monsalve_router
from .edwin_alejandro_manrique_rojas import router as edwin_alejandro_manrique_rojas_router
from .esteban_ortiz_medina import router as esteban_ortiz_medina_router
from .evelyn_tatiana_rojas_gutierrez import router as evelyn_tatiana_rojas_gutierrez_router
from .henry_mateo_castano_arias import router as henry_mateo_castano_arias_router
from .james_andres_estrada_diosa import router as james_andres_estrada_diosa_router
from .jhon_esteban_quintero_alzate import router as jhon_esteban_quintero_alzate_router
from .jhon_fredy_mena_miranda import router as jhon_fredy_mena_miranda_router
from .jimmy_alexander_correa import router as jimmy_alexander_correa_router
from .john_fabir_garrido_arenas import router as john_fabir_garrido_arenas_router
from .jose_alexis_arango_hernandez import router as jose_alexis_arango_hernandez_router
from .josmar_enrique_velasquez_urbina import router as josmar_enrique_velasquez_urbina_router
from .juan_camilo_ruiz_hoyos import router as juan_camilo_ruiz_hoyos_router
from .juan_carlos_arango_sarmiento import router as juan_carlos_arango_sarmiento_router
from .juan_david_vega_zapata import router as juan_david_vega_zapata_router
from .katherin_julieth_henao_perez import router as katherin_julieth_henao_perez_router
from .leidy_viviana_gomez_roman import router as leidy_viviana_gomez_roman_router
from .lemus_espinosa_claudia_patricia import router as lemus_espinosa_claudia_patricia_router
from .liceth_katherine_cano_velasquez import router as liceth_katherine_cano_velasquez_router
from .liliana_maria_garcia_ra_mirez import router as liliana_maria_garcia_ra_mirez_router
from .luis_felipe_zea_minota import router as luis_felipe_zea_minota_router
from .madelin_ruiz_mejia import router as madelin_ruiz_mejia_router
from .maria_angelica_bermudez_gutierrez import router as maria_angelica_bermudez_gutierrez_router
from .maria_camila_mona_henao import router as maria_camila_mona_henao_router
from .mariana_marin_ramirez import router as mariana_marin_ramirez_router
from .mateo_mejia_mejia import router as mateo_mejia_mejia_router
from .mayherlyn_lyset_salazar_echavarria import router as mayherlyn_lyset_salazar_echavarria_router
from .ronald_vasquez_losada import router as ronald_vasquez_losada_router
from .salome_alzate import router as salome_alzate_router
from .sara_jurado_giraldo import router as sara_jurado_giraldo_router
from .sebastian_giraldo_meza import router as sebastian_giraldo_meza_router
from .sebastian_londono_velez import router as sebastian_londono_velez_router
from .shirley_tatiana_torres_silva import router as shirley_tatiana_torres_silva_router
from .sthefanny_gomez_jerez import router as sthefanny_gomez_jerez_router
from .ubaldo_jose_meneses_pacheco import router as ubaldo_jose_meneses_pacheco_router
from .weiner_andres_valencia import router as weiner_andres_valencia_router
from .xiomara_giraldo_ocampo import router as xiomara_xiomara_giraldo_ocampo_router
from .yeniffer_elena_acosta_acosta import router as yeniffer_elena_acosta_acosta_router
from .yorman_alexis_david_lopez import router as yorman_alexis_david_lopez_router
from .yuliana_andrea_perez_tabares import router as yuliana_andrea_perez_tabares_router
from .yuliana_melissa_munoz_diossa import router as yuliana_melissa_munoz_diossa_router
from .yurany_alejandra_garcia_salazar import router as yurany_alejandra_garcia_salazar_router

app.include_router(andrey_perez_blandon_router)
app.include_router(camila_acevedo_machado_router)
app.include_router(camilo_andres_riascos_moran_router)
app.include_router(carlos_david_munoz_galeano_router)
app.include_router(carlos_felipe_campillo_gomez_router)
app.include_router(carolina_reina_pineda_router)
app.include_router(cindy_vanesa_castro_gomez_router)
app.include_router(cristhian_alexis_gallon_monsalve_router)
app.include_router(cristian_fernando_ricaurte_estrada_router)
app.include_router(dacier_dacier_escobar_chima_router)
app.include_router(daniel_felipe_guerra_rivera_router)
app.include_router(david_yusti_serna_router)
app.include_router(edison_jaramillo_monsalve_router)
app.include_router(edwin_alejandro_manrique_rojas_router)
app.include_router(esteban_ortiz_medina_router)
app.include_router(evelyn_tatiana_rojas_gutierrez_router)
app.include_router(henry_mateo_castano_arias_router)
app.include_router(james_andres_estrada_diosa_router)
app.include_router(jhon_esteban_quintero_alzate_router)
app.include_router(jhon_fredy_mena_miranda_router)
app.include_router(jimmy_alexander_correa_router)
app.include_router(john_fabir_garrido_arenas_router)
app.include_router(jose_alexis_arango_hernandez_router)
app.include_router(josmar_enrique_velasquez_urbina_router)
app.include_router(juan_camilo_ruiz_hoyos_router)
app.include_router(juan_carlos_arango_sarmiento_router)
app.include_router(juan_david_vega_zapata_router)
app.include_router(katherin_julieth_henao_perez_router)
app.include_router(leidy_viviana_gomez_roman_router)
app.include_router(lemus_espinosa_claudia_patricia_router)
app.include_router(liceth_katherine_cano_velasquez_router)
app.include_router(liliana_maria_garcia_ra_mirez_router)
app.include_router(luis_felipe_zea_minota_router)
app.include_router(madelin_ruiz_mejia_router)
app.include_router(maria_angelica_bermudez_gutierrez_router)
app.include_router(maria_camila_mona_henao_router)
app.include_router(mariana_marin_ramirez_router)
app.include_router(mateo_mejia_mejia_router)
app.include_router(mayherlyn_lyset_salazar_echavarria_router)
app.include_router(ronald_vasquez_losada_router)
app.include_router(salome_alzate_router)
app.include_router(sara_jurado_giraldo_router)
app.include_router(sebastian_giraldo_meza_router)
app.include_router(sebastian_londono_velez_router)
app.include_router(shirley_tatiana_torres_silva_router)
app.include_router(sthefanny_gomez_jerez_router)
app.include_router(ubaldo_jose_meneses_pacheco_router)
app.include_router(weiner_andres_valencia_router)
app.include_router(xiomara_xiomara_giraldo_ocampo_router)
app.include_router(yeniffer_elena_acosta_acosta_router)
app.include_router(yorman_alexis_david_lopez_router)
app.include_router(yuliana_andrea_perez_tabares_router)
app.include_router(yuliana_melissa_munoz_diossa_router)
app.include_router(yurany_alejandra_garcia_salazar_router)
