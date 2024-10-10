import subprocess
import os
import sys
import time

def create_public_connection():
    """SSH tüneli oluşturarak public bir bağlantı kurar"""
    file = "forward.txt"
    # SSH komutunu başlatma
    command = "ssh -R 80:0.0.0.0:4545 serveo.net -y > {} &".format(file)
    subprocess.Popen(command, shell=True)

    # Dosya içeriği yazılana kadar bekleme
    wait_time = 0
    while not os.path.exists(file) or os.stat(file).st_size == 0:
        time.sleep(1)
        wait_time += 1
        if wait_time > 15:  # 15 saniyeyi aşarsa hatalı bir durum olabilir
            print("SSH bağlantısı oluşturulamadı, lütfen tekrar deneyin.")
            sys.exit()

def get_public_url():
    """Public URL'yi elde eder"""
    ffile = "forward.txt"
    if os.path.exists(ffile):
        # Dosya içeriğini okuma ve veriyi elde etme
        with open(ffile, 'r') as file:
            read_data = file.read()

        # Veriyi işleme ve temizleme
        new_data = read_data.replace("Forwarding HTTP traffic from", "").strip()
        if new_data == "":
            print("Bağlantı alınamadı, lütfen tekrar deneyin.")
            sys.exit()
        else:
            return new_data
    else:
        print("Error: forward.txt dosyası mevcut değil.")
        sys.exit()
