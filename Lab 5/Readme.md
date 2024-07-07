# Securing Apache Web Server
## Setting Up Apache Server
At first we need to install apache web server in our machine using the following commands.
```bash
sudo apt update
sudo apt install apache2
```
Then run the following command.
```bash
sudo ufw allow 'Apache'
```
we can see the status of the apache webserver by using following command
```bash
sudo systemctl status apache2
```
Now we need to setup virtual hosts in our apache server.
For that, I used the following commands.
```bash
sudo mkdir /var/www/gci
```
Now we go to /var/www/gci/ directory using following command.
```bash
cd /var/www/gci/
```
Create an index.html file here using following command and paste the following code.
```bash
sudo nano index.html
```
```bash
<html>
<head>
  <title> Ubuntu rocks! </title>
</head>
<body>
  <p> I'm running this website on an Ubuntu Server server! </p>
</body>
</html>
```
Then go to /etc/apache2/sites-available/ directory and copy the content of deafult config to new gci config using the following command.
```
cd /etc/apache2/sites-available/
sudo cp 000-default.conf gci.conf
```
Then change the ServerName, DocumentRoot, ServerAdmin using the following command. <br> For me, ServerName gci.example.com, DocumentRoot /var/www/gci/ and ServerAdmin hamim@example.com
```bash
sudo nano gci.conf
```
After setting up our website, we need to activate the virtual hosts configuration file to enable it. <br> We do that by running the following command in the configuration file directory
```bash
sudo a2ensite gci.conf
```
We can also see if anything went wrong in our setup by the following command.
```bash
sudo apache2ctl configtest
```
Then we need to restart our server using the following command to activate the virtual host.
```bash
sudo service apache2 reload
```
Now we can go to gci.example.com in our browser and see the contents of our index.html file.  <br>
If the browser can't reach gci.examle.com then we need to add hosts in /etc/hosts/ file using the following command. <br>
For me, I had to add 127.0.0.1 to gci.example.com
```bash
sudo nano /etc/hosts
```
The result is here
![image](https://github.com/hamim-33/Information_Security_Lab/assets/102356771/02216d16-a01f-4f6e-9c90-bc03f57f7962)

## Now Comes the part of Securing the Server.
First, we need to generate a private key and a self-signed certificate using OpenSSL using the following command.
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache.key -out /etc/ssl/certs/apache.crt
```

Once we complete providing the information, the openssl command should generate a private key and a certificate file in the following locations.
```
/etc/ssl/private/apache.key
/etc/ssl/certs/apache.crt
```
Then Edit the config file.
```bash
sudo nano /etc/apache2/sites-available/gci.conf
```
And update with the following configuration.
```
<VirtualHost *:443>
    ServerAdmin hamim@example.com
    ServerName gci.example.com
    DocumentRoot /var/www/gci

    SSLEngine on
    SSLCertificateFile    /etc/ssl/certs/apache.crt
    SSLCertificateKeyFile /etc/ssl/private/apache.key

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Enable the SSL module and the SSL site configuration and restart the apache server.
```bash
sudo a2enmod ssl
sudo a2ensite gci.conf
sudo systemctl restart apache2
```
Enable the firewall and allow traffic on ports 80 and 443.
```bash
sudo ufw enable
sudo ufw allow 'Apache Full'
sudo ufw allow 'ssh'
```
Check the firewall status to ensure the rules are applied correctly.
```bash
sudo ufw status
```
Then we can test the new configuratiob by visitng the secured site "https://gci.example.com". <br>
Here, we see a warning because the certificate is self-signed, but we can proceed to verify the encryption.
![image](https://github.com/hamim-33/Information_Security_Lab/assets/102356771/1ba86d6a-b176-4438-a27f-28d3309153b2)








