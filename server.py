import os
import csv
import socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
from collections import namedtuple

User = namedtuple("User", "username password user_type")

"""
Explanation of permissions as described in the source code of pyftpdlib:

Read permissions:
 - "e" = change directory (CWD command)
 - "l" = list files (LIST, NLST, STAT, MLSD, MLST, SIZE, MDTM commands)
 - "r" = retrieve file from the server (RETR command)

Write permissions:
 - "a" = append data to an existing file (APPE command)
 - "d" = delete file or directory (DELE, RMD commands)
 - "f" = rename file or directory (RNFR, RNTO commands)
 - "m" = create directory (MKD command)
 - "w" = store a file to the server (STOR, STOU commands)
 - "M" = change file mode (SITE CHMOD command)
 - "T" = update file last modified time (MFMT command)
"""


def main():
    users = get_users()
    authorizer = DummyAuthorizer()

    private_files = "/Repository/"
    shared_files = "/Repository/Shared/"

    # Sets home folder and permissions for each user
    for user in users:

        if user.user_type == "admin":
            home = os.getcwd() + private_files
            permissions = "elradfmwMT"
        elif user.user_type == "friend":
            home = os.getcwd() + shared_files
            permissions = "elrafmwMT"
        else:
            print("Error: user type '" + user.user_type + "' is invalid.")
            continue

        authorizer.add_user(user.username, user.password, home, permissions)

    handler = FTPHandler
    handler.banner = "Hello World!"
    handler.authorizer = authorizer
    handler.masquerade_address = get_local_ip()
    handler.passive_ports = range(60000, 65535)

    server = FTPServer(("0.0.0.0", 21), handler)
    server.max_cons = 200
    server.max_cons_per_ip = 10

    server.serve_forever()


# Reads user accounts from a .csv file
def get_users():
    users = []

    with open("users.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True)

        next(csv_reader)  # Skips the first row

        for row in csv_reader:
            users.append(User(row[0], row[1], row[2]))

        print("Users:")
        for user in users:
            print(user.username + ", " + user.password + ", " + user.user_type)

    return users


# Gets the local IP of the machine the server is running on
# The code for this was found here: https://stackoverflow.com/a/28950776/11562557
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    main()
