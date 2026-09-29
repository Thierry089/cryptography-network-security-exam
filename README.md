# Cryptography and Network Security Exam

## 1. Project Overview

This project was developed as part of the Cryptography and Network Security examination.

The project demonstrates basic security controls for a polytechnic institute that stores student records on a central server and transfers files between campuses.

The project covers:

* Risk assessment
* File encryption and decryption
* SHA-256 integrity verification
* Firewall traffic filtering
* Security testing
* Documentation and evidence

---

## 2. Project Structure

```text
cryptography-network-security-exam/
│
├── README.md
├── risk_assessment.md
├── encryption_tool.py
├── sample_student_record.txt
├── filter_tests.md
└── .gitignore
```

### File Descriptions

| File                        | Purpose                                                                           |
| --------------------------- | --------------------------------------------------------------------------------- |
| `README.md`                 | Project documentation, installation and execution instructions                    |
| `risk_assessment.md`        | Identifies assets, vulnerabilities, risks and recommended controls                |
| `encryption_tool.py`        | Python program for encryption, decryption and integrity checking                  |
| `sample_student_record.txt` | Sample student record used for testing                                            |
| `filter_tests.md`           | Firewall configuration and connection test evidence                               |
| `.gitignore`                | Prevents sensitive/generated files such as the encryption key from being uploaded |

The encryption key is stored locally and is not committed to the repository.

---

# 3. Requirements

The following are required to run the Python application:

* Python 3
* Python `cryptography` library
* Linux/Windows/macOS computer

The firewall testing requires an authorised laboratory environment with appropriate network access.

---

# 4. Installation

## Step 1: Install Python

Install Python 3 on the computer.

Verify the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

## Step 2: Install the Cryptography Library

Run:

```bash
pip install cryptography
```

If required, use:

```bash
pip3 install cryptography
```

---

# 5. Running the Encryption Program

Place the sample student record in the project directory.

The supplied sample file is:

```text
sample_student_record.txt
```

Run the program using:

```bash
python encryption_tool.py sample_student_record.txt
```

The program performs the following operations:

1. Generates an encryption key if one does not already exist.
2. Loads the encryption key.
3. Encrypts the student record.
4. Saves the encrypted file.
5. Decrypts the encrypted file.
6. Compares the decrypted file with the original.
7. Calculates the SHA-256 hash.
8. Saves the hash.
9. Checks whether the original file has been modified.

---

# 6. Expected Encryption Output

After successfully running the program, the following files are generated locally:

```text
secret.key
student_record.enc
student_record_decrypted.txt
student_record.sha256
```

The encryption key is sensitive and must not be uploaded to GitHub.

The `.gitignore` file prevents these sensitive/generated files from being committed.

---

# 7. Testing File Integrity

The SHA-256 hash is used to detect changes to the student record.

After running the program, modify the contents of:

```text
sample_student_record.txt
```

For example, change:

```text
GPA: 3.45
```

to:

```text
GPA: 3.10
```

Run the program again.

The SHA-256 value will be different because the contents of the file have changed.

This demonstrates the ability of the integrity check to detect file modification.

---

# 8. Firewall Configuration

The firewall was configured in the authorised laboratory environment.

The configuration was designed to:

1. Block guest network access to the student records server.
2. Permit the authorised staff network to access the service specified by the assessor.
3. Block other inbound access to that service.

The firewall configuration and testing procedure are documented in:

```text
filter_tests.md
```

Example UFW commands used in the laboratory include:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

The actual IP addresses, networks and service ports should correspond to the values provided by the assessor.

---

# 9. Reproducing the Firewall Tests

The firewall tests should be performed only in the authorised laboratory environment.

Three tests were performed:

### Test 1 — Permitted Connection

A connection from the authorised staff network to the specified service should succeed.

Example:

```bash
ssh <username>@<server-ip>
```

Expected result:

```text
Connection allowed.
```

### Test 2 — Blocked Guest Connection

A connection from the guest network to the student records server should be blocked.

Example:

```bash
ssh <username>@<server-ip>
```

Expected result:

```text
Connection blocked.
```

### Test 3 — Blocked Unauthorised Connection

A connection from a network other than the authorised staff network to the specified service should be blocked.

Expected result:

```text
Connection blocked.
```

The commands, expected results and actual results are documented in:

```text
filter_tests.md
```

---

# 10. Security Considerations

The project follows several basic security practices:

* Student records are encrypted before storage or transmission.
* SHA-256 is used to detect changes to files.
* Guest network access to the records server is restricted.
* Only authorised staff network traffic is permitted to the specified service.
* Other inbound access is blocked.
* The encryption key is kept outside the GitHub repository.
* The project uses fictional sample student information rather than real student records.

---

# 11. GitHub Repository

The complete project contains the source code, risk assessment, firewall testing documentation and project instructions.

Repository:

`<PASTE YOUR GITHUB REPOSITORY URL HERE>`
