### FTP Server

Based on [pyftpdlib](https://github.com/giampaolo/pyftpdlib).


This is a simple FTP (File Transfer Protocol) server which allows sharing of files over the internet or on a local network. This server is not secure at all since it does not use any encryption (because firewalls and routers really do not like encrypted FTP, Windows explorer doesn't like it either, which I wanted to use as an FTP client).

When the code runs, it will expect a couple of folders and files to be present, it will crash if they don't exist. Those files and folders are not included in the repo.


Two of the folders that it expects are named in the variables "private_files" and "shared_files". These different folders are available to different "user types". For example the "admin" user type will have access to "private_files" while others do not. The user accounts will be read from the file "users.csv" while the different user types for these accounts can be found in code. If this file doesn't exist the program will crash. The structure of the file is like this: 

| username | password | user_type |
| -------- | -------- | --------- |
| examplename | examplepassword | admin |
