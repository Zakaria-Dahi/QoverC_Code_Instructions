#Import Generic Python Packages
import numpy as np
from scipy.optimize import minimize
#Import Qiskit Python Packages for Building the Hamiltonian and the QAOA Ansatz
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
#Import Qiskit Python Package for the QAOA Ansatz Transpilation
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
#Import Qiskit Python Package for the Qiskit Estimator and Sampler Primitives
from qiskit.primitives import StatevectorEstimator
from qiskit.primitives import StatevectorSampler


# Build The Problem Hamiltonian, and its Corresponding Ansatz
pauli_list = []
pauli_list.append(("ZZ", [0, 1], -3))
pauli_list.append(("Z", [0], 3))
pauli_list.append(("Z", [1], 3))
pauli_list.append(("Z", [2], 1))
cost_hamiltonian = SparsePauliOp.from_sparse_list(pauli_list, 3)
cost_circuit = QAOAAnsatz(cost_operator=cost_hamiltonian, reps=2)


#Assign Initial Values to QAOA Ansatz Parameters
initial_gamma = np.pi
initial_beta = np.pi / 2
init_params = [initial_beta, initial_beta, initial_gamma, initial_gamma]

# Transpile the QAOA Ansatz to ISA Format: Instruction Set Architecture
pm = generate_preset_pass_manager(optimization_level=1)
isa_circuit = pm.run(cost_circuit)
isa_hamiltonian = cost_hamiltonian.apply_layout(isa_circuit.layout)


# Set Up and Run the Qiskit Estimator
def cost_func_estimator(params, ansatz, hamiltonian, estimator):
    job_estimator = estimator.run([(ansatz, hamiltonian, params)])
    results = job_estimator.result()[0]
    cost = results.data.evs
    return cost

estimator = StatevectorEstimator()
estimation_result = minimize(
        cost_func_estimator,
        init_params,
        args=(isa_circuit, isa_hamiltonian, estimator),
        method="COBYLA",
        tol=1e-2,
    )

# Set Up and Run the Qiskit Sampler
sampler = StatevectorSampler()
isa_circuit.measure_all()
job = sampler.run([(isa_circuit,estimation_result.x)],shots=int(1e3))
counts_int = job.result()[0].data.meas.get_int_counts()
counts_bin = job.result()[0].data.meas.get_counts()
shots = sum(counts_int.values())
final_distribution_int = {key: val / shots for key, val in counts_int.items()}
final_distribution_bin = {key: val / shots for key, val in counts_bin.items()}



# Display the QAOA Ansatz
print(cost_circuit.decompose().decompose())
# Display the Optimised QAOA Ansatz Parameters
print(estimation_result)
# Display the QAOA Solution Sampling Distribution
print(final_distribution_bin)

