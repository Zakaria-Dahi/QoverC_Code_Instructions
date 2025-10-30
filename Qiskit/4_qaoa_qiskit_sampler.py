# Set Up and Run the Qiskit Sampler
sampler = StatevectorSampler()
isa_circuit.measure_all()
job = sampler.run([(isa_circuit,estimation_result.x)],shots=int(1e3))
counts_int = job.result()[0].data.meas.get_int_counts()
counts_bin = job.result()[0].data.meas.get_counts()
shots = sum(counts_int.values())
final_distribution_int = {key: val / shots for key, val in counts_int.items()}
final_distribution_bin = {key: val / shots for key, val in counts_bin.items()}