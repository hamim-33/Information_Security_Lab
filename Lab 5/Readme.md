# Securing Apache Web Server
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

