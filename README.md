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

    C = (P + K) mod 26

### Decryption

    P = (C - K) mod 26

Where:

- `P` = Plaintext
- `C` = Ciphertext
- `K` = Encryption Key

### Example

    Plaintext  : HELLO
    Key        : 3
    Ciphertext : KHOOR

Decryption:

    Ciphertext : KHOOR
    Key        : 3
    Plaintext  : HELLO

## 🖥️ Application Screenshots

### Fig 1 — Dashboard / Cipher Console

The main Cipher Console provides the core encryption and decryption functionality.

![Fig 1 - Dashboard / Cipher Console](https://res.cloudinary.com/wpop4xyo/image/upload/v1790598332/Screenshot_2026-09-28_174256.png)

### Fig 2 — Brute-Force Attack Lab

The Brute-Force Attack Lab demonstrates the weakness of Caesar Cipher by testing all 26 possible keys against a ciphertext.

![Fig 2 - Brute-Force Attack Lab](https://res.cloudinary.com/wpop4xyo/image/upload/v1790598333/Screenshot_2026-09-28_174539.png)

### Fig 3 — Frequency Analysis

Frequency Analysis demonstrates how character-frequency patterns can expose weaknesses in simple substitution ciphers.

![Fig 3 - Frequency Analysis](https://res.cloudinary.com/wpop4xyo/image/upload/v1790598332/Screenshot_2026-09-28_174836.png)

### Fig 4 — Character Mapping

The Character Mapping module displays the transformation between plaintext and ciphertext alphabets for the selected key.

![Fig 4 - Character Mapping](https://res.cloudinary.com/wpop4xyo/image/upload/v1790598332/Screenshot_2026-09-28_175007.png)

### Fig 5 — Automated Test Center

The Automated Test Center validates encryption, decryption, round-trip recovery, wrong-key behavior, and input validation.

![Fig 5 - Automated Test Center](https://res.cloudinary.com/wpop4xyo/image/upload/v1790598333/Screenshot_2026-09-28_175101.png)

## 🏗️ Project Structure

    CAESAR-CIPHER-SECURITY-LAB/
    │
    ├── app.py
    ├── cipher_engine.py
    ├── cryptanalysis.py
    ├── security_analysis.py
    ├── database.py
    ├── data/
    │   └── cipher_lab.db
    │── Caesar_Cipher_Presentation (PPT)
    │
    ├── requirements.txt
    ├── .gitignore
    └── README.md

### Module Responsibilities

| Module | Purpose |
|---|---|
| `app.py` | Streamlit application and user interface |
| `cipher_engine.py` | Caesar Cipher encryption, decryption and character mapping |
| `cryptanalysis.py` | Brute-force attack, frequency analysis and round-trip verification |
| `security_analysis.py` | Input validation and security analysis |
| `database.py` | SQLite audit logging |
| `requirements.txt` | Python dependencies |

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application and cryptographic logic |
| **Streamlit** | Interactive web application |
| **SQLite** | Local audit logging |
| **Git & GitHub** | Version control and project hosting |

## ⚙️ Installation & Setup

### 1. Clone the Repository

    git clone https://github.com/Atharva-ark06/CAESAR-CIPHER-SECURITY-LAB.git
    cd CAESAR-CIPHER-SECURITY-LAB

### 2. Create a Virtual Environment

    python -m venv venv

### 3. Activate the Environment

**Windows PowerShell:**

    venv\Scripts\Activate.ps1

### 4. Install Dependencies

    pip install -r requirements.txt

### 5. Run the Application

    streamlit run app.py

The application will open in your browser.

## 🔍 Security Analysis

The Caesar Cipher has significant security limitations:

- Only **26 possible keys**
- Vulnerable to brute-force attacks
- Vulnerable to frequency analysis
- Uses a simple substitution mechanism
- Provides no modern authentication or integrity protection
- Not suitable for protecting confidential real-world information

The Security Lab demonstrates these weaknesses through practical attack simulations.

## 🧪 Testing

The Automated Test Center includes:

| Test | Purpose |
|---|---|
| Encryption Test | Verifies plaintext → ciphertext |
| Decryption Test | Verifies ciphertext → plaintext |
| Round-Trip Test | Confirms original plaintext is recovered |
| Wrong-Key Test | Demonstrates incorrect decryption |
| Empty Input Test | Verifies input validation |

## 📚 Educational Purpose

This project was developed as an **Information Security / Cryptography practical project** to understand:

- Classical cryptography
- Encryption and decryption
- Cryptographic keys
- Cipher transformations
- Brute-force attacks
- Frequency analysis
- Security weaknesses
- Input validation
- Security testing
- Audit logging

> **Note:** Caesar Cipher is intended for educational demonstration and should not be used to protect sensitive or confidential information.

## 👨‍💻 Author

**Atharva Kulkarni**

B.Tech Computer Science & Engineering  
G M University, Davangere

GitHub: https://github.com/Atharva-ark06

## ⭐ Project

If you find this project useful for learning classical cryptography and cybersecurity concepts, consider giving the repository a ⭐.
