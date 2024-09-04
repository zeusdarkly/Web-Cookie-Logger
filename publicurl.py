import subprocess
import os
import sys

def create_public_connection():
    file = "forward.txt"
    command = "ssh -R 80:0.0.0.0:4545 serveo.net -y > {} &".format(file)
    subprocess.Popen(command, shell=True)

def get_public_url():
    ffile = "forward.txt"
    if os.path.exists(ffile):
        # Dosyanın içeriğini temizle
        with open(ffile, 'w') as file:
            file.write("")  # Dosyanın içeriğini temizler
        with open(ffile, 'r') as file:
            read_data = file.read()
        new_data = read_data.replace("Forwarding HTTP traffic from", "")
        new_data = new_data.replace("\n", "")
        new_data = new_data.replace("\r", "")
        if new_data == "":
            print("Please restart.....")
            sys.exit()
        else:
            return new_data
    else:
        print("Error: forward.txt does not exist.")
        sys.exit()