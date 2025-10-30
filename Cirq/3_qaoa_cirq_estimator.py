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
    sample_results = cirq_simulator.sample(qaoa_ansatz_optimised, params=params, \
                                                                   repetitions=int(1e3))
    return estimate_cost(sample_results)

min_energy = float('inf')
for i in range(grid_size):
    for j in range(grid_size):
        if min_energy > energy_from_params(i*gamma_max/grid_size, j*beta_max/grid_size, \ 
                                                                       qaoa_ansatz_optimised):
           min_energy = energy_from_params(i*gamma_max/grid_size, j*beta_max/grid_size, \
                                                                       qaoa_ansatz_optimised)
           best_gamma = i * gamma_max / grid_size
           best_beta = i * beta_max / grid_size 