import math
from qiskit import QuantumCircuit

# Basic Encoding Method

desired_state = [
    0,
    0,
    0,
    0,
    0,
    1 / math.sqrt(2),
    0,
    1 / math.sqrt(2)
]

circ = QuantumCircuit(3)
circ.initialize(desired_state, [0, 1, 2])
circ.decompose().decompose().decompose().decompose().decompose().draw()
