import subprocess
import os
import sys

def create_public_connection():
    file = "forward.txt"
    command = "ssh -R 80:0.0.0.0:4545 serveo.net -y > {} &".format(file)
    subprocess.Popen(command, shell=True)

def get_public_url():
    ffile = "forward.txt"
    try:
        with open(ffile, 'r') as file:
            read_data = file.read()
        os.remove(ffile)
        new_data = read_data.replace("Forwarding HTTP traffic from", "").strip().replace("\n", "").replace("\r", "")
        if not new_data:
            print("Please restart.....")
            sys.exit()
        else:
            return new_data
    except PermissionError:
        print(f"Hata: {ffile} dosyası başka bir işlem tarafından kullanılıyor.")
        sys.exit()
    except Exception as e:
        print(f"Hata: {ffile} dosyasını işlerken bir hata oluştu: {e}")
        sys.exit()
