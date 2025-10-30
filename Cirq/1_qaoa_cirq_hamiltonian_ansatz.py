# Assign Initial Values to QAOA Ansatz Parameters
gamma = sympy.Symbol("gamma")
beta = sympy.Symbol("beta")
gamma_value = np.pi / 4
beta_value = np.pi / 2

# Build The Problem Hamiltonian, and its Corresponding Ansatz
qubits_register = cirq.LineQubit.range(3)
qaoa_ansatz = cirq.Circuit(cirq.H.on_each(qubits_register))
qaoa_ansatz.append(cirq.ZZ(qubits_register[0],qubits_register[1]) ** (gamma_value * -6))
qaoa_ansatz.append(cirq.Z(qubits_register[0]) ** (gamma_value * 6))
qaoa_ansatz.append(cirq.Z(qubits_register[1]) ** (gamma_value * 6))
qaoa_ansatz.append(cirq.Z(qubits_register[2]) ** (gamma_value * -2))
for index_qubit in range(3):
    qaoa_ansatz.append(cirq.X(qubits_register[index_qubit]) ** beta_value)
qaoa_ansatz.append(cirq.M(qubits_register))