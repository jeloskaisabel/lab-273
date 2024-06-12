import http.client
import sys

def getRfcText(rfc_number):
    connection = http.client.HTTPSConnection("www.ietf.org")
    request_url = f'/rfc/rfc{rfc_number}.txt'
    
    try:
        connection.request("GET", request_url)
        response = connection.getresponse()

        if response.status == 200:
            data = response.read()
            return data
        else:
            print(f"Error al descargar el RFC {rfc_number}: {response.status} {response.reason}")
            return None
    finally:
        connection.close()

def saveToFile(rfc_number, text):
    #Guarda el texto del RFC en un archivo
    if text:
        filename = f'RFC{rfc_number}.txt'
        with open(filename, 'wb') as file:
            file.write(text)
        print(f"El RFC {rfc_number} ha sido guardado exitosamente en {filename}")
    else:
        print("No se recibio texto para guardar")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Introduzca un numero de RFC!")
        sys.exit(1)

    rfcNumber = sys.argv[1]
    rfcText = getRfcText(rfcNumber)
    saveToFile(rfcNumber, rfcText)

