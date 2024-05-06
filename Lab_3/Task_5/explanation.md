#### Command used for the hashing and the output for the hash:
###### 03:56:44 hamim@hamim-zorin Security_Lab → openssl dgst -md5 text_file.txt 
###### MD5(text_file.txt)= d41d8cd98f00b204e9800998ecf8427e
###### 04:23:09 hamim@hamim-zorin Security_Lab → openssl dgst -sha256 text_file.txt
###### SHA256(text_file.txt)= e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
###### 04:23:47 hamim@hamim-zorin Security_Lab → openssl dgst -sha512 text_file.txt
###### SHA512(text_file.txt)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

##### MD5:
Hash value: d41d8cd98f00b204e9800998ecf8427e \
MD5 produces a 128-bit (32-character hexadecimal) hash value. \
It's widely used but considered weak for cryptographic purposes due to vulnerabilities. 

##### SHA256:
Hash value: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 \
SHA-256 produces a 256-bit (64-character hexadecimal) hash value. \
It's widely adopted and offers stronger security than MD5.

##### SHA512:
Hash value: cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e \
SHA-512 produces a 512-bit (128-character hexadecimal) hash value. \
It provides even stronger security than SHA-256 and is suitable for applications requiring high security. 
