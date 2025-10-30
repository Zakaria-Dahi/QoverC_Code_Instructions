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