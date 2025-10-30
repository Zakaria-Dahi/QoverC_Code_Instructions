# Import Generic Python Packages
import numpy as np
from scipy.optimize import minimize
# Import Qiskit Python Packages for Building the Hamiltonian and the QAOA Ansatz
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
# Import Qiskit Python Package for the QAOA Ansatz Transpilation
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
# Import Qiskit Python Package for the Qiskit Estimator and Sampler Primitives
from qiskit.primitives import StatevectorEstimator
from qiskit.primitives import StatevectorSampler