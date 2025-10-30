# Display the QAOA Ansatz
print(cost_circuit.decompose().decompose())
# Display the Optimised QAOA Ansatz Parameters
print(estimation_result)
# Display the QAOA Solution Sampling Distribution
print(final_distribution_bin)