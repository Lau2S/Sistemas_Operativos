#
#
# Este script define un hilo que se encarga de calcular la posicion 'n' en la
# serie de Fibonacci.
#
# Aurores:
# Gabriela Guzmán - guzman.gabriela@correounivalle.edu.co
# Laura Stefania Salazar - laura.blanco@correounivalle.edu.co
# Juliana Melissa Bolaños - juliana.araujo@correounivalle.edu.co
#
# Fecha: 2024-10-16
#
from fibonacci import fibo
from time import time
import multiprocessing
import sys

class FiboWorker(multiprocessing.Process):
  def __init__(self, vector, pid):
    multiprocessing.Process.__init__(self)
    self.vector = vector
    self._pid = pid

  def run(self):
    self.vector[self._pid] = fibo(self.vector[self._pid])
    print(f"[{self._pid}] Fibonacci calculado: {self.vector[self._pid]}")

def main():
    vector = multiprocessing.Array('i', [33] * 144)  # Vector de 144 posiciones, inicializado con 33
    num_cpus = multiprocessing.cpu_count()  # Número de CPUs disponibles
    print(f"Procesando un vector de longitud {len(vector)} en {num_cpus} CPUs")

    procesos = []  # Vector de procesos
    ts = time()  # Tomar el tiempo inicial

    # Crear un proceso por cada posición del vector
    for pid in range(len(vector)):
        print(f"Trabajador {pid} comienza")
        worker = FiboWorker(vector, pid)
        worker.start()
        procesos.append(worker)

    # Esperar a que todos los procesos terminen
    for worker in procesos:
        worker.join()

    print(f"Proceso completo. Tiempo total: {time() - ts} segundos")
 

if __name__ == "__main__":
    main()


