import socket
import json
import urllib.parse

# Diccionario de estilos del cuerpo del QR
body_styles = {
    "1": "square", "2": "mosaic", "3": "dot", "4": "circle", "5": "circle-zebra",
    "6": "circle-zebra-vertical", "7": "circular", "8": "edge-cut",
    "9": "edge-cut-smooth", "10": "japanese", "11": "leaf", "12": "pointed",
    "13": "pointed-edge-cut", "14": "pointed-in", "15": "pointed-in-smooth",
    "16": "pointed-smooth", "17": "round", "18": "rounded-in",
    "19": "rounded-in-smooth", "20": "rounded-pointed", "21": "star", "22": "diamond"
}

# Diccionario de estilos de ojos
eye_options = {
    "0": "frame0", "1": "frame1", "2": "frame2", "3": "frame3", "4": "frame4",
    "5": "frame5", "6": "frame6", "7": "frame7", "8": "frame8", "9": "frame9",
    "10": "frame10", "11": "frame11", "12": "frame12", "13": "frame13",
    "14": "frame14", "15": "frame15", "16": "frame16"
}

# Diccionario de estilos de pupilas
eye_ball_options = {
    "1": "ball1", "2": "ball2", "3": "ball3", "4": "ball4", "5": "ball5",
    "6": "ball6", "7": "ball7", "8": "ball8", "9": "ball9", "10": "ball10",
    "11": "ball11", "12": "ball12", "13": "ball13", "14": "ball14", "15": "ball15",
    "16": "ball16", "17": "ball17", "18": "ball18", "19": "ball19"
}

def select_option(prompt, options):
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Elige una opción: ")
    return options.get(choice, None)

def get_qr_data():
    print("Selecciona el tipo de dato:")
    data_types = ["URL", "Texto Plano", "Email", "Teléfono", "SMS"]
    for index, type in enumerate(data_types, start=1):
        print(f"{index}. {type}")
    type_index = int(input("Opción: ")) - 1
    data = input("Ingresa información para tu QR: ")

    data_formats = [
        lambda x: urllib.parse.quote(x),
        lambda x: x,
        lambda x: f"mailto:{x}",
        lambda x: f"tel:{x}",
        lambda x: f"sms:{x}?body={urllib.parse.quote(input('Mensaje SMS: '))}"
    ]
    data = data_formats[type_index](data)

    body = select_option("Elige la forma del cuerpo del QR:", body_styles)
    eye = select_option("Elige el estilo de los ojos del QR:", eye_options)
    eye_ball = select_option("Elige el estilo de las pupilas del QR:", eye_ball_options)
    color_body = input("Ingresa el color del cuerpo del QR en formato hexadecimal (ej. #FF0000): ")
    size = int(input("Ingresa el tamaño del código QR (de 100 a 1000 pixels): "))
    format = select_option("Formato de descarga:", {"1": "png", "2": "svg", "3": "pdf", "4": "eps"})
    logo = input("¿Deseas agregar un logo al código QR? Proporciona la ruta del archivo si es así: ")

    return {
        "data": data,
        "body": body,
        "eye": eye,
        "eyeBall": eye_ball,
        "color_body": color_body,
        "size": size,
        "format": format,
        "logo": logo
    }

def send_request_to_server(qr_data):
    host = 'localhost'
    port = 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(json.dumps(qr_data).encode('utf-8'))
        response = sock.recv(1024)
        print("Response from server:", response.decode('utf-8'))

if __name__ == "__main__":
    qr_data = get_qr_data()
    send_request_to_server(qr_data)
