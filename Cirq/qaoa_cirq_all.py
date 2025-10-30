# Import Generic Python Packages
import numpy as np
import pandas as pd
from collections import Counter
import sympy
# Import Cirq Package
import cirq



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


# Transpile the QAOA Ansatz using Cira Transforñers
def optimize_circuit(circuit, context=None, k=2):
    # Merge 2-qubit Connected Components into Circuit Operations.
    optimized_circuit = cirq.merge_k_qubit_unitaries(circuit, k=k, \
                               rewriter=lambda op: op.with_tags("merged"), context=context)
    # Drop Operations With Negligible Effect / Close to Identity.
    optimized_circuit = cirq.drop_negligible_operations(optimized_circuit, context=context)
    # Expand all remaining merged connected components.
    optimized_circuit = cirq.expand_composite(optimized_circuit, \
                            no_decomp=lambda op: "merged" not in op.tags, context=context)
    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit, \
                                                                        optimized_circuit)
    return optimized_circuit
qaoa_ansatz_optimised = optimize_circuit(qaoa_ansatz)

# Set Up and Run the Cirq Optimiser Using Grid Search
cirq_simulator = cirq.Simulator()
grid_size = 2
gamma_max = 2
beta_max = 2

def estimate_cost(samples: pd.DataFrame) -> float:
    cost_value = 0.0
    sampled_strings=[]
    for index, row in samples.iterrows():
        sampled_strings.append(row['q(0),q(1),q(2)'])
    stats= Counter(sampled_strings)
    for key,value in stats.items():
        stats[key] = stats[key]/1e3
        solution = cirq.big_endian_int_to_bits(int(key), bit_count=3)
        fitness = (-12*solution[0]*solution[1]) + (2*solution[2])
        cost_value = cost_value + stats[key]*fitness      
    return cost_value

def energy_from_params(gamma_value: float, beta_value: float, qaoa: cirq.Circuit) -> float:
    params = cirq.ParamResolver({"gamma": gamma_value, "beta": beta_value})
    sample_results = cirq_simulator.sample(qaoa_ansatz_optimised, params=params, repetitions=int(1e3))
    return estimate_cost(sample_results)

min_energy = float('inf')
for i in range(grid_size):
    for j in range(grid_size):
        if min_energy > energy_from_params(i * gamma_max / grid_size, j * beta_max / grid_size, qaoa_ansatz_optimised):
           min_energy = energy_from_params(i * gamma_max / grid_size, j * beta_max / grid_size, qaoa_ansatz_optimised)
           best_gamma = i * gamma_max / grid_size
           best_beta = i * beta_max / grid_size           

# Set Up and Run the Cirq Sampler
sample_results = cirq_simulator.sample(qaoa_ansatz_optimised, params={gamma: best_gamma, beta: best_beta}, repetitions=int(1e3))

# Display the QAOA Ansatz
print(qaoa_ansatz)
# Display the Optimised QAOA Ansatz Parameters
print(f'The best gamma value is:{best_gamma}')
print(f'The best beta value is:{best_beta}')
# Display the QAOA Solution Sampling Distribution
sampled_strings = []
sample_distribution = {}
for index, row in sample_results.iterrows():
    sampled_strings.append(row['q(0),q(1),q(2)'])
stats= Counter(sampled_strings)
for key,value in stats.items():
    value = stats[key]/1e3
    key = cirq.big_endian_int_to_bits(int(key), bit_count=3)
    sample_distribution[str(key)]=value
print(sample_distribution)