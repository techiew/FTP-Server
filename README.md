## FTP Server

Uses [pyftpdlib](https://github.com/giampaolo/pyftpdlib). 

To download the required packages, first create and activate a python virtual environment and then run this command:

```pip install -r requirements.txt```


This is a simple FTP (File Transfer Protocol) server which allows sharing of files over the internet or on a local network. This server is not secure at all since it does not use any encryption.


### Requirements to run
When the code runs, it will expect a couple of folders and files to be present in the root folder, it will crash if they don't exist. Those files and folders are not included in the repo.


Two of the folders that it expects are named in the variables "private_files" and "shared_files". These different folders are available to different user types when they connect to the server. For example the "admin" user type will have access to "private_files" while others might only have access to the folder pointed to by "shared_files". 


The user accounts used for logging into the server will be fetched from the file "users.csv" (see [how CSV works](https://www.computerhope.com/issues/ch001356.htm)) while the different user types available for these accounts can be found in code. If "users.csv" doesn't exist the program will crash. The structure of the file is like this: 

| username | password | user_type |
| -------- | -------- | --------- |
| examplename | examplepassword | admin |
| anotherexample | anotherpassword | admin |

(The header needs to be included in the actual file, also there has to be newlines at the end of each row)
