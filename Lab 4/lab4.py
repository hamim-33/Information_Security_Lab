import argparse
import hashlib
import time
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

# AES Key Generation
def generate_aes_key(length, key_file):
    key = get_random_bytes(length)
    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"AES key of length {length * 8} bits generated and saved to {key_file}")

# RSA Key Generation
def generate_rsa_key(bits, private_key_file, public_key_file):
    key = RSA.generate(bits)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open(private_key_file, 'wb') as f:
        f.write(private_key)
    with open(public_key_file, 'wb') as f:
        f.write(public_key)
    print(f"RSA key pair of {bits} bits generated and saved to {private_key_file} and {public_key_file}")

# AES Encryption/Decryption
def aes_encrypt_decrypt(file_path, key_path, mode, operation, output_file):
    with open(key_path, 'rb') as f:
        key = f.read()

    cipher = AES.new(key, mode)
    if operation == 'encrypt':
        with open(file_path, 'rb') as f:
            data = f.read()
        padded_data = pad(data, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
    elif operation == 'decrypt':
        with open(file_path, 'rb') as f:
            ciphertext = f.read()
        padded_data = cipher.decrypt(ciphertext)
        data = unpad(padded_data, AES.block_size)
        with open(output_file, 'wb') as f:
            f.write(data)
        print(data.decode())

# RSA Encryption/Decryption
def rsa_encrypt_decrypt(file_path, key_path, operation, output_file):
    with open(key_path, 'rb') as f:
        key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(key)
    if operation == 'encrypt':
        with open(file_path, 'rb') as f:
            data = f.read()
        ciphertext = cipher.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
    elif operation == 'decrypt':
        with open(file_path, 'rb') as f:
            ciphertext = f.read()
        data = cipher.decrypt(ciphertext)
        with open(output_file, 'wb') as f:
            f.write(data)
        print(data.decode())

# RSA Signature
def rsa_sign_verify(file_path, key_path, operation, sig_file):
    with open(key_path, 'rb') as f:
        key = RSA.import_key(f.read())

    with open(file_path, 'rb') as f:
        data = f.read()

    if operation == 'sign':
        h = SHA256.new(data)
        signature = pkcs1_15.new(key).sign(h)
        with open(sig_file, 'wb') as f:
            f.write(signature)
    elif operation == 'verify':
        with open(sig_file, 'rb') as f:
            signature = f.read()
        h = SHA256.new(data)
        try:
            pkcs1_15.new(key).verify(h, signature)
            print("The signature is valid.")
        except (ValueError, TypeError):
            print("The signature is not valid.")

# SHA-256 Hashing
def sha256_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    hash_object = hashlib.sha256(data)
    print(hash_object.hexdigest())

# Main Command Line Interface
def main():
    parser = argparse.ArgumentParser(description="Crypto Operations")
    parser.add_argument('operation', choices=['gen_aes_key', 'gen_rsa_key', 'aes_enc', 'aes_dec', 'rsa_enc', 'rsa_dec', 'rsa_sign', 'rsa_verify', 'sha256'], help='Crypto operation to perform')
    parser.add_argument('file_path', nargs='?', help='Path to the file to operate on')
    parser.add_argument('--key_path', help='Path to the key file', required=False)
    parser.add_argument('--mode', choices=['ECB', 'CFB'], help='Mode for AES', required=False)
    parser.add_argument('--output', help='Path to the output file', required=False)
    parser.add_argument('--sig_file', help='Path to the signature file', required=False)
    parser.add_argument('--length', type=int, choices=[16, 32], help='Length of AES key (in bytes)', required=False)
    parser.add_argument('--private_key', help='Path to save the RSA private key', required=False)
    parser.add_argument('--public_key', help='Path to save the RSA public key', required=False)
    parser.add_argument('--bits', type=int, help='Bit length for RSA key', required=False)
    args = parser.parse_args()

    start_time = time.time()
    
    if args.operation == 'gen_aes_key':
        generate_aes_key(args.length, args.key_path)
    elif args.operation == 'gen_rsa_key':
        generate_rsa_key(args.bits, args.private_key, args.public_key)
    elif args.operation == 'aes_enc':
        aes_encrypt_decrypt(args.file_path, args.key_path, AES.MODE_ECB if args.mode == 'ECB' else AES.MODE_CFB, 'encrypt', args.output)
    elif args.operation == 'aes_dec':
        aes_encrypt_decrypt(args.file_path, args.key_path, AES.MODE_ECB if args.mode == 'ECB' else AES.MODE_CFB, 'decrypt', args.output)
    elif args.operation == 'rsa_enc':
        rsa_encrypt_decrypt(args.file_path, args.key_path, 'encrypt', args.output)
    elif args.operation == 'rsa_dec':
        rsa_encrypt_decrypt(args.file_path, args.key_path, 'decrypt', args.output)
    elif args.operation == 'rsa_sign':
        rsa_sign_verify(args.file_path, args.key_path, 'sign', args.sig_file)
    elif args.operation == 'rsa_verify':
        rsa_sign_verify(args.file_path, args.key_path, 'verify', args.sig_file)
    elif args.operation == 'sha256':
        sha256_hash(args.file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time for {args.operation}: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    main()
