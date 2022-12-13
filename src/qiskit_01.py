from qiskit import QuantumCircuit, transpile
from qiskit_aer.backends import AerSimulator

simulator = AerSimulator()

circ = QuantumCircuit(2, 2)
circ.h([0, 1])
circ.cx(0, 1)
circ.measure([0, 1], [0, 1])
compiled_circ = transpile(circ, simulator)

job = simulator.run(compiled_circ, shots=1024)
results = job.result()
counts = results.get_counts()

print(counts)
