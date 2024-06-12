import socket

def serverEco():
    host = '127.0.0.1'
    port = 7777

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Servidor iniciado. Esperando clientes...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexión desde: {addr}")

        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data or data.strip().lower() == "adios":
                break
            conn.send(data.encode('utf-8'))
        
        conn.close()
        print("Conexión cerrada.")
        if data.strip().lower() == "adios":
            break

    server_socket.close()
    print("Servidor detenido.")

if __name__ == "__main__":
    serverEco()
