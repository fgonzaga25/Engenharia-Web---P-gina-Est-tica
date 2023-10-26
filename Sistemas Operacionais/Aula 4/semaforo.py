import threading
import time

recurso_compartilhado = []
mutex = threading.Semaphore(1)
semaforo_contador = threading.Semaphore(0)
contador = 0

def leitor():
    global contador
    while True:
        semaforo_contador.acquire()
        print(f"Leitor lendo: {recurso_compartilhado}")
        semaforo_contador.release()
        time.sleep(1)

def escritor():
    global contador
    while True:
        mutex.acquire()
        recurso_compartilhado.append("Nova informação")
        print(f"Escritor escrevendo: {recurso_compartilhado}")
        mutex.release()
        semaforo_contador.release()
        time.sleep(2)

for _ in range(3):
    threading.Thread(target=leitor).start()

for _ in range(2):
    threading.Thread(target=escritor).start()
