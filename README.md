# QoverC_Code_Instructions
<div align="center">
<img src="https://github.com/Zakaria-Dahi/QoverC/blob/main/assets/img/3d_logo.gif">
</div>

**Programmer:** Zakaria Abdelmoiz DAHI et al. :shipit:

**About:** 

  - This repository contains the instructions for the source code contained in the paper:  ``QoverC: A Profiler of Quantum Computer Simulators for Quantum Optimisation``. 
  - The repository is organised in three directories:
    - :open_file_folder: **Cirq:** contains a fragmented and standalone implementation of the quantum approximate optimisation algorithm for solving QUBOs using Google Cirq SDK.
      - :page_facing_up: ``0_qaoa_cirq_packages.py``: Imports the necessary Python packages.
      - :page_facing_up: ``1_qaoa_cirq_hamiltonian_ansatz.py``: Builds up the problem Hamiltonian and ansatz.  
      - :page_facing_up: ``2_qaoa_cirq_transformer.py``: Applies the transformer pass over the ansatz.  
      - :page_facing_up: ``3_qaoa_cirq_estimator.py``: Sets and runs the ansatz estimator.  
      - :page_facing_up: ``4_qaoa_cirq_sampler.py``: Sets and runs the ansatz sampler. 
      - :page_facing_up: ``5_qaoa_cirq_display.py``: Displays the results of the execution.
      - :page_facing_up: ``qaoa_cirq_all.py``: Executes all the aforementioned steps from one single script.


    - :open_file_folder: **Qiskit:** contains a fragmented and standalone implementation of the quantum approximate optimisation algorithm for solving QUBOs using IBM Qiskit SDK.
      - :page_facing_up: ``0_qaoa_qiskit_packages.py``: Imports the necessary Python packages.
      - :page_facing_up: ``1_qaoa_qiskit_hamiltonian_ansatz.py``: Builds up the problem Hamiltonian and ansatz.  
      - :page_facing_up: ``2_qaoa_qiskit_transpilation.py``: Applies the transpilation pass over the ansatz.    
      - :page_facing_up: ``3_qaoa_qiskit_estimator.py``: Sets and runs the ansatz estimator.  
      - :page_facing_up: ``4_qaoa_qiskit_sampler.py``: Sets and runs the ansatz sampler.   
      - :page_facing_up: ``5_qaoa_qiskit_display.py``: Displays the results of the execution.  
      - :page_facing_up: ``qaoa_qiskit_all.py``: Executes all the aforementioned steps from one single script.  


    - :open_file_folder: **Ocean:** contains a fragmented and standalone implementation for applying the quantum annealer for solving QUBOs using D-Wave Ocean SDK.   
      - :page_facing_up: ``qa_ocean.py``: Builds up from a single script the problem instance, sets the solver, and runs the experiment.
