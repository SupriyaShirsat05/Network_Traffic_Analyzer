# Network Traffic Analyzer using Machine Learning
A Computer Networks + Machine Learning project that analyzes network traffic and detects SYN Flood attacks using packet-level features extracted from real network traffic generated in Mininet.

# Project Overview
This project demonstrates how realistic network traffic can be generated, captured, processed, and analyzed using machine learning techniques to detect malicious behavior (SYN Flood attacks).

# Procedure
-> Real network traffic generation using Mininet

-> Packet capture using tcpdump

-> Feature extraction using Wireshark / Tshark

-> Dataset balancing to avoid ML bias

-> Machine Learning classification

# Problem Statement
Detect SYN Flood attacks in network traffic by analyzing packet-level features and classifying traffic as:
Normal traffic
Attack traffic (SYN Flood)

# Note on High Accuracy
The machine learning model in this project achieves very high (sometimes near-perfect) accuracy, which may appear unrealistic at first glance. This behavior is expected and justified due to the controlled nature of the dataset and experimental setup.

Why high accuracy occurs in this project:
* Controlled traffic environment
* Distinct attack characteristics

SYN flood attacks exhibit strong and easily distinguishable patterns such as:
* Repeated SYN packets
* Abnormal TCP flag combinations
* Similar packet sizes
* High packet rate in short time intervals

These features make classification easier for ML models.
