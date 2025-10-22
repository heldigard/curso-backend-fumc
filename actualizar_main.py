import os

archivos = [f for f in os.listdir("clase2-api-tareas") if f.endswith(".py") and f != "main.py" and not f.startswith(".")]

imports = []
includes = []

for archivo in archivos:
    nombre_modulo = archivo[:-3]  # quitar .py
    imports.append(f"from .{nombre_modulo} import router as {nombre_modulo}_router")
    includes.append(f"app.include_router({nombre_modulo}_router)")

with open("clase2-api-tareas/main.py", "a", encoding="utf-8") as f:
    f.write("\n# Routers de estudiantes\n")
    for imp in imports:
        f.write(imp + "\n")
    f.write("\n")
    for inc in includes:
        f.write(inc + "\n")

print("Routers agregados a main.py")
