# Threads, Processes and Sequential

## Members

* Juliana Melissa Bolaños - 2372224
* Laura Stefania Salazar Blanco - 2327896
* Gabriela Guzmán Botina - 2326772

## Description

This repository contains the files of an exercise for the Operating Systems class

The main objective of the exercise is to compare the performance of a program when using different ways of implementation: threads, processes and sequential.

## Results of the executions
365.99572253227234
480.8745367527008
381.70160937309265
459.6579751968384
| Execution | Sequential (s)    | Thread (s)      | Process (s)      |
|-----------|-------------------|-----------------|------------------|
| 1         |162.82550048828125|398.99877643585205|43.961246490478516|
| 2         |165.39500522613525|365.99572253227234|44.149916648864746|
| 3         |163.2106578350067 |480.8745367527008 |43.9959990978241  |
| 4         |162.3547601699829 |381.70160937309265|43.73776936531067 |
| 5         |243.42437410354614|459.6579751968384 |43.96547603607178 |
| *Average* |163.81039         |413.452787001     |43.974            |

The average is calculated with the remaining values by eliminating the longest and the shortest time
