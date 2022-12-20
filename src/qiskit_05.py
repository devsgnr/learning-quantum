# Training Parameterized Quantum Circuits
from qiskit.circuit.library import RealAmplitudes

anstaz = RealAmplitudes(num_qubits=2, reps=1, insert_barriers=True).decompose()
anstaz.draw()
