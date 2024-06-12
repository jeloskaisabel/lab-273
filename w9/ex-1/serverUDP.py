from socket import *

def getFibonacciTerm(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
    return str(a)

def runServer():
    PORT = 21567
    ADDR = ('', PORT)
    
    srvsock = socket(AF_INET, SOCK_DGRAM)
    srvsock.bind(ADDR)
    print(f"Servidor activo y escuchando en el puerto {PORT}...")

    try:
        while True:
            data, addr = srvsock.recvfrom(512)
            client_ip, client_port = addr
            print(f'Solicitud recibida de {client_ip}:{client_port}')
            
            try:
                n = int(data.decode())
                
                ans = getFibonacciTerm(n)
                response = f'El {n} término de la serie de Fibonacci: {ans}'
                print(f'{n} término de la serie de Fibonacci enviado')
            except ValueError:
                response = "Error: Entrada no válida"
                print(f"Entrada no válida recibida de {client_ip}:{client_port}")
            srvsock.sendto(response.encode(), addr)
    finally:
        srvsock.close()

if __name__ == '__main__':
    runServer()
