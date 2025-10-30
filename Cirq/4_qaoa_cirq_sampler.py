# Set Up and Run the Cirq Sampler
sample_results = cirq_simulator.sample(qaoa_ansatz_optimised, params={gamma: best_gamma, \ 
                                                 beta:best_beta}, repetitions=int(1e3))
