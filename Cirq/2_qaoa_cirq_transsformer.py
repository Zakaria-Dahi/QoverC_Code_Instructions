# Transpile the QAOA Ansatz using Examples of Cirq Transformers
def optimize_circuit(circuit, context=None, k=2):
    # Merge 2-qubit Connected Components into Circuit Operations.
    optimized_circuit = cirq.merge_k_qubit_unitaries(circuit, k=k, \
                               rewriter=lambda op: op.with_tags("merged"), context=context)
    # Drop Operations With Negligible Effect / Close to Identity.
    optimized_circuit = cirq.drop_negligible_operations(optimized_circuit, context=context)
    # Expand all Remaining Merged Connected Components.
    optimized_circuit = cirq.expand_composite(optimized_circuit, \
                            no_decomp=lambda op: "merged" not in op.tags, context=context)
    # Assert the Original and Optimized Circuit are Equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit, \
                                                                        optimized_circuit)
    return optimized_circuit
qaoa_ansatz_optimised = optimize_circuit(qaoa_ansatz)