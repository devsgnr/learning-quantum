from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

circuit = QuantumCircuit(2)
theta = Parameter('θ')

circuit.rz(theta, 0)
circuit.crz(theta, 1, 0)
circuit.draw()
