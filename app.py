from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Universidad")
agregar_tarea(tareas, "Preparar laboratorio", "Universidad")
agregar_tarea(tareas, "Comprar materiales", "Personal")
completar_tarea(tareas, 1)

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')

print("\nPendientes de Universidad:")
for tarea in pendientes(tareas, "universidad"):
    print(f'- {tarea["id"]}: {tarea["titulo"]}')
