# Set Up and Run the Qiskit Estimator
def cost_func_estimator(params, ansatz, hamiltonian, estimator):
    job_estimator = estimator.run([(ansatz, hamiltonian, params)])
    results = job_estimator.result()[0]
    cost = results.data.evs
    return cost

estimator = StatevectorEstimator()
estimation_result = minimize(cost_func_estimator, init_params, \
        args=(isa_circuit, isa_hamiltonian, estimator), method="COBYLA", tol=1e-2)