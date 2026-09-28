# 🔐 Caesar Cipher Security Lab

> An interactive cryptography laboratory built with Python, Streamlit, and SQLite for demonstrating Caesar Cipher encryption, decryption, cryptanalysis, security weaknesses, and automated testing.

## 📌 Overview

The **Caesar Cipher Security Lab** is an educational cybersecurity application that demonstrates how a classical substitution cipher works and why it is considered insecure for modern data protection.

The application provides an interactive environment for:

- Encryption and decryption
- Character mapping
- Cryptographic model visualization
- Brute-force attack simulation
- Frequency analysis
- Round-trip verification
- Automated security testing
- Local audit logging
- Security analysis

## 🚀 Features

### 🔒 Core Cryptography

- Caesar Cipher encryption
- Caesar Cipher decryption
- User-defined cipher key
- Uppercase and lowercase character support
- Preservation of spaces and punctuation
- Automatic key normalization

### 🧪 Security Laboratory

- **Brute-Force Attack Lab** — tests all 26 possible keys
- **Frequency Analysis** — analyzes character frequency
- **Character Mapping** — displays plaintext-to-ciphertext mapping
- **Round-Trip Verification** — verifies encryption and decryption integrity
- **Automated Test Center** — executes positive and negative test cases
- **Security Analysis** — demonstrates the limitations of the cipher

### 📋 Audit & Validation

- Input validation
- Empty-input protection
- Message length validation
- SQLite-based operation history
- Timestamped audit records
- Local security activity tracking

## 🧠 Cryptographic Model

### Encryption

```text
C = (P + K) mod 26
