# Transpile the QAOA Ansatz to ISA Format: Instruction Set Architecture
pm = generate_preset_pass_manager(optimization_level=1)
isa_circuit = pm.run(cost_circuit)
isa_hamiltonian = cost_hamiltonian.apply_layout(isa_circuit.layout)