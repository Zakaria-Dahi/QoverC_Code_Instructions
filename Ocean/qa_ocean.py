# Import Ocean Python Packages
import dimod
from dwave.system import EmbeddingComposite
from dwave.system import DWaveSampler

# Building up the Quadratic Formulation of the Problem
qubo = {(0, 0): 0, (1, 1): 0, (2, 2): 2,(0, 1): -12}
bqm = dimod.BQM.from_qubo(qubo)

# Define the Solver Embedding Process
sampler = EmbeddingComposite(DWaveSampler())

# Solve the problem using the Quantum Sampler
sample_results = sampler.sample_qubo(bqm, num_reads=5000)

# Display the Sampling Results
print(f"Solution: sample={sample_results}")