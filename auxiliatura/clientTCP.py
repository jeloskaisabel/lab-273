import socket
import sys
import os

def clientTCP():
    if len(sys.argv) != 2:
        print("Ingrese el nombre del archivo!!")
        return

    host = '127.0.0.1'
    port = 7778

    download_folder = 'descargas'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    file_name = sys.argv[1]
    client_socket.send(file_name.encode('utf-8'))

    full_path = os.path.join(download_folder, file_name)
    with open(full_path, 'wb') as file:
        while True:
            bytes_read = client_socket.recv(4096)
            if not bytes_read:
                break
            file.write(bytes_read)
    
    client_socket.close()
    print("[+] Archivo descargado")

if __name__ == "__main__":
    clientTCP()
