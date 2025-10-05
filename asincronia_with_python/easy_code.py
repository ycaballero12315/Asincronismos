import asyncio
import time
import threading

async def receta(plato, tiempo):
    thread_id = threading.current_thread().name
    if plato == 'tostadas':
        raise RuntimeError('Pan quemado!')
    print(f'[{thread_id}] 🍳 Comenzamos : {plato}')
    await asyncio.sleep(tiempo)
    print(f"[{thread_id}] ✅ Terminado plato: {plato} en: {tiempo:.2f}")

async def cocinando():
    start = time.perf_counter()
    elemts ={
        'Amburguesa': 2,
        'Arroz': 1,
        'vegetable': 4,
        'tostadas': 2
    }
    print('Comenzamos a cocinar: ')
    result = await asyncio.gather(
        *(receta(elem, t) for elem, t in elemts.items()),
        return_exceptions=True
    )
    for r in result:
        if isinstance(r, Exception):
            print(f"⚠️ Error en la receta: {r}")

    print('Tarea de cocina terminada...')

    end = time.perf_counter()
    print(f'La rutina se demoro ⏱️{end-start:.2f}s')
    print(f'💡Todo en el mismo hilo')

async def cocinando_ejec_con_contexto():
    print('Uso de contexto...')
    start = time.perf_counter()
    elemts ={
        'Amburguesa': 2,
        'Arroz': 1,
        'vegetable': 4,
        'tostadas': 2
    }
    print('Comenzamos a cocinar: ')
    try:
        async with asyncio.TaskGroup() as tg:
            print('Comenzando todo en marcha al mismo tiempo>>>')
            [tg.create_task(receta(p,t)) for p,t in elemts.items()]
        print('Tarea de cocina terminada...')

    except* RuntimeError as eg:
        print('---'*10)
        for e in eg.exceptions:
            print(f'Error en la cocina! error: {e}')
        print('---'*10)

    end = time.perf_counter()
    print(f'La rutina se demoro ⏱️{end-start:.2f}s')
    print(f'💡Todo en el mismo hilo')

if __name__ == "__main__":
   asyncio.run(cocinando_ejec_con_contexto())
