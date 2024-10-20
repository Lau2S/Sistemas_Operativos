#
#
# Este script se encarga de procesar los elementos de un vector de longitud 144 usando la versión con Threads.
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
import threading
import sys

class FiboWorker(threading.Thread):
  def __init__(self, tid, s, e, y, vectorR):
    threading.Thread.__init__(self)
    self.s = s
    self.e = e
    self.y = y
    self.tid = tid
    self.vectorR = vectorR

  def run(self):
    for x in range(self.s, self.e):
      self.vectorR[x] = fibo(self.y) # guarda el fibonacci de 33 en la posicion de x
      print(f"[Trabajador {self.tid}]: Fibonacci de {self.y} es {fibo(self.y)}")

def main():
  max_fibo = 33
  if len(sys.argv) > 1:
    max_fibo = int(sys.argv[1])
  num_cpus = multiprocessing.cpu_count() # CPUs disponibles
  print(f"Calculando el fibonacci {max_fibo} con {num_cpus} cpus")
  vectorR =  [max_fibo] * 144 # vector que tiene 144 veces el numero 33
  hilos = []
  size = len(vectorR)//num_cpus # tamaño de cuántos elementos del vectorR le corresponde a cada hilo de ejecución
  ts = time() # se toma tiempo

  for x in range(num_cpus): # Ciclo para crear trabajadores
    print(f"Trabajador {x+1} comienza")
    s = x * size
    e = (x + 1) * size if x != num_cpus - 1 else len(vectorR)
    worker = FiboWorker((x+1), s, e,  vectorR[x], vectorR)
    worker.start()
    hilos.append(worker)

  for x in range(num_cpus): # Ciclo para esperar por trabajadores
    print(f"Esperando por trabajador {x+1}")
    hilos[x].join()

  print(f"Tomo {time() - ts}")


if __name__ == "__main__":
   main()
