from socket import *
import sys

def runClient():
    HOST = 'localhost'
    PORT = 21567
    
    clisock = socket(AF_INET, SOCK_DGRAM)
    
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("Introduza un número: "))
    
    message = str(n).encode()
    clisock.sendto(message, (HOST, PORT))
    print(f'{n} término de la serie Fibonacci solicitado a {HOST}:{PORT}')

    response, _ = clisock.recvfrom(512)
    print("Respuesta recibida del servidor:", response.decode())

    clisock.close()

if __name__ == '__main__':
    runClient()
