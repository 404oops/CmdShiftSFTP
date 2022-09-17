import paramiko
from time import sleep
import os
import subprocess
import string
import random
def copycb(output):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))
paramiko.util.log_to_file("paramiko.log")
transport = paramiko.Transport(("Host", 22)) # Change the host (and port if necessary)
transport.connect(None, 'username', "password") # you can add a private key by replacing the password with pkey=paramiko.RSAKey.from_private_key_file("/path/to/id_rsa")
sftp = paramiko.SFTPClient.from_transport(transport)
endpoint = "" # enter your HTTP folder where the file will be located, for example: "https://example.com/images/"
destination = "" # Enter your server directory where the images will be uploaded to. This doesn't have to do anything with the HTTP server, for example: "/data/files/images/"
# Make sure to add a trailing slash at the end of both of these properties
while True:
    ls = os.listdir("images")
    if len(ls) != 0:
        if ls[0].endswith(".png") or ls[0].endswith(".mov"):
            from bar import *
            toupload = "images/" + ls[0]
            if ls[0].endswith(".png"): ext = "png"
            if ls[0].endswith(".mov"): ext = "mov"
            fn = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 10)) + "." + ext
            copycb(" " + endpoint + fn + " ")
            sftp.put(os.getcwd() + "/" + toupload, destination + fn, callback=cbk)
            os.remove(toupload)
    sleep(0.5)
    try: 
        pass
    except KeyboardInterrupt:
        sftp.close()
        transport.close()
        exit()