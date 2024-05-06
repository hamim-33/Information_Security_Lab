###### 04:24:00 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcde" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= 16a7c3bbf6a4db2480e541a4ea6d77cd8db58f942ffb5a9766116f1896bf55cb226fbcc811380cd09adbe02d8e2c1e1be18d3f8940dd0a63a1ad79aff8575a3a
###### 04:39:10 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefgh" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= da8ec3b3deda60f96d11b9e8f9aa7ae5ffc7d8ab7dab541e69ce7c939584e1ce4c6ec25d9087e06aeece91d522e0d6e3c6f28236ec5706b73408ff1ab62f38d2
###### 04:39:29 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefghabcd" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= 6edc9fd87153cdf1901a670df401d5775e3612210870e5b1c0033a71b5921cf520b3cd8cb250181c80bf0a0b3aa42cfff5f1fd0c613a7ba9d74dfbae8f187739
###### 04:40:02 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefghabcd" -md5 text_file.txt
##### HMAC-MD5(text_file.txt)= 2054282820b5fd8ae4bed440f3f160ad
###### 04:40:59 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefgh" -md5 text_file.txt
##### HMAC-MD5(text_file.txt)= 44ab1aed82e58ddeedf5564ce62f7257
###### 04:41:17 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcde" -md5 text_file.txt
##### HMAC-MD5(text_file.txt)= 4e552a909f75dceee923df96529b64c2
###### 04:41:30 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcde" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= 16a7c3bbf6a4db2480e541a4ea6d77cd8db58f942ffb5a9766116f1896bf55cb226fbcc811380cd09adbe02d8e2c1e1be18d3f8940dd0a63a1ad79aff8575a3a
###### 04:42:19 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefgh" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= da8ec3b3deda60f96d11b9e8f9aa7ae5ffc7d8ab7dab541e69ce7c939584e1ce4c6ec25d9087e06aeece91d522e0d6e3c6f28236ec5706b73408ff1ab62f38d2
###### 04:42:33 hamim@hamim-zorin Security_Lab → openssl dgst -hmac "abcdefghabcd" -sha512 text_file.txt
##### HMAC-SHA512(text_file.txt)= 6edc9fd87153cdf1901a670df401d5775e3612210870e5b1c0033a71b5921cf520b3cd8cb250181c80bf0a0b3aa42cfff5f1fd0c613a7ba9d74dfbae8f187739
## Observations:
### When using HMAC-SHA512 with different keys ("abcde", "abcdefgh", "abcdefghabcd"), the HMAC values are different.
### Similarly, with HMAC-MD5, the HMAC values vary with different keys.
### The length of the key seems to influence the HMAC value, as seen in the difference between "abcde" and "abcdefgh" for both SHA512 and MD5.
### However, for HMAC-SHA512, using a longer key ("abcdefghabcd") does not necessarily result in a longer HMAC value compared to a shorter key ("abcdefgh").
