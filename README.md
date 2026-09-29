# Cryptography and Network Security Exam

## Project Description

This project is a small Python security toolkit developed for the
Cryptography and Network Security examination.

The toolkit demonstrates:
- File encryption and decryption
- SHA-256 integrity checking
- Detection of file modification
- Basic error handling

- ## Technologies Used

- Python 3
- Cryptography library
- Fernet symmetric encryption
- SHA-256 hashing
- GitHub

- ## Installation

Install Python 3 and then install the required cryptography library:

```bash
pip install cryptography


**5. How to run it**

Also specifically required:

```markdown
## Execution

Run the following command:

```bash
python encryption_tool.py sample_student_record.txt


what happens(Explanations):

```markdown
The program will:
1. Generate an encryption key.
2. Encrypt the student record.
3. Save the encrypted file.
4. Decrypt the file.
5. Compare the decrypted file with the original.
6. Calculate the SHA-256 hash.
7. Check whether the file has been modified.


## Security

The encryption key is stored locally and is not uploaded to GitHub.
The `.gitignore` file prevents the key and generated files from
being committed to the repository.
