# Build The Problem Hamiltonian, and its Corresponding Ansatz
pauli_list = []
pauli_list.append(("ZZ", [0, 1], -3))
pauli_list.append(("Z", [0], 3))
pauli_list.append(("Z", [1], 3))
pauli_list.append(("Z", [2], 1))
cost_hamiltonian = SparsePauliOp.from_sparse_list(pauli_list, 3)
cost_circuit = QAOAAnsatz(cost_operator=cost_hamiltonian, reps=2)


# Assign Initial Values to QAOA Ansatz Parameters
initial_gamma = np.pi
initial_beta = np.pi / 2
init_params = [initial_beta, initial_beta, initial_gamma, initial_gamma]
