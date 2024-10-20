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
  def __init__(self, n, pid):
    multiprocessing.Process.__init__(self)
    self.n = n
    self._pid = pid

  def run(self):
    print(f"[{self._pid}] Fibonacci de {self.n} es {fibo(self.n)}")

def main():
  max_fibo = 33
  if len(sys.argv) != 1:
    max_fibo = int(sys.argv[1])
  num_cpus = multiprocessing.cpu_count() # CPUs disponibles
  print(f"Calculando el fibonacci {max_fibo} en {num_cpus} CPUs")
  procesos = [ ] # Vector de procesos
  ts = time() # se toma tiempo
  for x in range(144): # Ciclo para crear trabajadores
    print(f"Trabajador {x} comienza")
    worker = FiboWorker(max_fibo,x)
    worker.start()
    procesos.append(worker)

  for worker in procesos: # Ciclo para esperar por trabajadores
    print(f"Esperando por trabajador {worker._pid}")
    worker.join()

  print(f"Tomo {time() - ts}")


if __name__ == "__main__":
  main()
