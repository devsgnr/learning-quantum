from qiskit import QuantumCircuit, transpile
from qiskit.providers.basicaer import QasmSimulatorPy

# Setup Simulator - QasmSimulatorPy
simulator = QasmSimulatorPy()


# Design a circuit with a 2 qubit register and 2 bit classical register
# Put qubit [0] and [1] in superposition using Hadamard gate
# Entangle qubit [0] to [1] using the CX (CNOT) gate
# Measure outcome on respective classical register
circ = QuantumCircuit(2, 2)
circ.h([0, 1])
circ.cx(0, 1)
circ.measure([0, 1], [0, 1])
compiled_circ = transpile(circ, simulator)

# Set up job on QasmSimulator and get the result
job = simulator.run(compiled_circ, shots=1024)
results = job.result()
counts = results.get_counts()

# Print the counts of probabilities
print(counts)
