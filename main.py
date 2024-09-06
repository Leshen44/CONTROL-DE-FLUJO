estudiantes = [
    {"nombre": "Juan", "edad": 17, "calificaciones": [85, 90, 88]},
    {"nombre": "María", "edad": 19, "calificaciones": [92, 89, 90]},
    {"nombre": "Pedro", "edad": 21, "calificaciones": [85, 95, 80]},
    {"nombre": "Ana", "edad": 18, "calificaciones": [90, 92, 87]},
    {"nombre": "Luis", "edad": 20, "calificaciones": [88, 85, 92]},
]
nota = 0


for x in estudiantes:
    cant = 0
    nota = 0
    n = x.get("calificaciones")
    print (x["calificaciones"])
    e = x.get("edad")
    for i in n:
        nota += i
        cant += 1
    promedio = nota / cant
    if e >= 18 and e % 2 == 1:
        print(f"el estudiante tiene un promedio {promedio:.2f} y edad {e}")
