# csc8820-vnf-simulator

# Introduction
Virtual Network Function (VNF) chain is a chain of different network functions (NF). Each network function is an application level service such as Firewall, Intrusion Detection System, Encoder, etc, .... Data packets may flow through these services in an established order. A specific order of these network functions/services is called a service chain. Virtualization technique allows the service chain to be deployed into the cloud in a flexible way that can satisfy different objectives such as minimizing deployment cost, or maximizing the service performance. 

In this project, we deploy a framework to test various strategies for Virtual Network Function (VNF) deployment. For each strategy, there is a way to split a given a VNF chain into a list of sub-chains, and a way to assign sub-chains to physical machines. Therefore, the characteristics of the network traffic between these NFs in the chain are different. The CPU cost of each physical machine for each deployment strategy will also be different.

The developed framework in this project will measure different criteria such as delay, bandwidth consumption, and CPU cost for each deployment strategy and verify the performance of our proposed deployment algorithm.

# How to use our program
All the code to generate simulated data and visualization is in the file simulate_delay.ipynb. Simply start a jupyter notebook server and run line by line the Python code in the file simulate_delay.ipynb to regenerate the results.
