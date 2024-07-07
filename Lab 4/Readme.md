# Lab 4: Programming Symmetric & Asymmetric Crypto
## AES Encryption
First we need to generate the keys for AES Encryption.
To generate keys, we use the following commands
```bash
python3 lab4.py gen_aes_key --length 16 --key_path aes_key_16.bin
python3 lab4.py gen_aes_key --length 32 --key_path aes_key_32.bin
```
Then we need to encrypt our target file using the keys. For that we use the following commands.
Here, I used 128 bits and ECB mode. You can use CFB mode and 256 bits also.
```bash
python3 lab4.py aes_enc test.txt --key_path aes_key_16.bin --mode ECB --output encrypted_aes.bin
cat encrypted_aes.bin
```
To decrypt the encrypted file we use the following commands.
```bash
python3 lab4.py aes_dec encrypted_aes.bin --key_path aes_key_16.bin --mode ECB --output decrypted_aes.bin
cat decrypted_aes.bin
```
## RSA Encryption
Now For RSA encryption we need to generate the RSA keys first.
For that, we use the following commands. You can generate 2048 bits keys also.
```bash
python3 lab4.py gen_rsa_key --bits 1024 --private_key private_1024.pem --public_key public_1024.pem
```
Now to encrypt a file using RSA encryption, we use the following command.
```bash
python3 lab4.py rsa_enc test.txt --key_path public_1024.pem --output encrypted_rsa.bin
```
To decrypt, we use the following command.
```bash
python3 lab4.py rsa_dec encrypted_rsa.bin --key_path private_1024.pem --output decrypted_rsa.bin
```
To sign a file using RSA encryption, we use the following command.
```bash
python lab4.py rsa_sign test.txt --key_path private_2048.pem --sig_file signature.bin
```
And To verify signature, we use the following command.
```bash
python3 lab4.py rsa_verify test.txt --key_path public_2048.pem --sig_file signature.bin
```
## SHA-256 Encryption
To encrypt using sha-256, we use the following command.
```bash
python3 lab4.py sha256 test.txt
```

This script provides a flexible command-line interface for performing AES and RSA operations while measuring and displaying the execution time for each operation, allowing for performance analysis across different key sizes.
