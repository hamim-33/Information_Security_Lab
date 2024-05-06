###### 04:54:53 hamim@hamim-zorin Security_Lab → openssl dgst -md5 input.txt 
##### MD5(input.txt)= be9321e93ada409862432d73370ddb58
###### 04:55:20 hamim@hamim-zorin Security_Lab → openssl dgst -sha256 input.txt 
##### SHA256(input.txt)= c89c5aa89c6d0a8b97e418a279a4e6225adb09b8043a980575f8b48e5b3674fc
###### 05:01:43 hamim@hamim-zorin Security_Lab → openssl dgst -md5 modified_input.txt 
##### MD5(modified_input.txt)= e46152896b927bf8725ffa84a6e263c1
###### 05:05:26 hamim@hamim-zorin Security_Lab → openssl dgst -sha256 modified_input.txt 
##### SHA256(modified_input.txt)= fce0d20c16ba9b6f0eb9c5b70ba06a92d8174b8a534a2e766a634826f3732e4c
### Observations:
#### Both MD5 and SHA256 hashes are different between the original and modified files.
#### Modifying even a single bit in the input file results in significant changes in the hash values.
#### The MD5 and SHA256 hash algorithms demonstrate their property of avalanche effect, where a small change in the input leads to a drastically different output hash value.
#### The modified file's hash values (H2) are distinct from the original file's hash values (H1), indicating that the hash functions are sensitive to changes in the input data.
