import socket
import os

def serverTCP():
    host = '127.0.0.1'
    port = 7778

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor iniciado. Esperando clientes...")

    base_folder = "archivos-servidor"

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión desde: {addr}")
        
        data = conn.recv(1024).decode('utf-8')
        if not data:
            conn.close()
            continue
        
        file_path = os.path.join(base_folder, data.strip())
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                while True:
                    bytes_read = file.read(4096)
                    if not bytes_read:
                        break
                    conn.sendall(bytes_read)
        else:
            conn.send("Archivo no encontrado.".encode('utf-8'))
        
        conn.close()

if __name__ == "__main__":
    serverTCP()
