import string
from collections import Counter
evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

partes = evaluar.split(":")
titulo = partes[1].split()
if ((len(titulo)) <= (11)):
    print("titulo: ok")
else:
    print("titulo: mal")
oraciones = partes[2].split(".")

ok1 = 0
ok2 = 0
ok3 = 0
ok4 = 0

for oracion in oraciones:
    palabras = oracion.split()
    cant = len(palabras)
    match cant:
        case cant if cant <= 12:
            ok1 += 1
        case  cant if cant >12 and cant <18:
            ok2 += 1
        case  cant if cant >17 and cant <24:
            ok3 += 1       
        case _:
            ok4 += 1   

print("Cantidad de oraciones fáciles de leer: ", ok1," aceptables para leer: ", ok2, " dificil de leer: ",ok3, " muy difícil de leer: ",ok4)