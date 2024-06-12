import requests
import json
import urllib.parse

# Opciones predefinidas
body_styles = [
    "square", "mosaic", "dot", "circle", "circle-zebra", "circle-zebra-vertical", "circular",
    "edge-cut", "edge-cut-smooth", "japanese", "leaf", "pointed", "pointed-edge-cut",
    "pointed-in", "pointed-in-smooth", "pointed-smooth", "round", "rounded-in",
    "rounded-in-smooth", "rounded-pointed", "star", "diamond"
]

eye_options = {
    "0": "frame0", "1": "frame1", "2": "frame2", "3": "frame3", "4": "frame4",
    "5": "frame5", "6": "frame6", "7": "frame7", "8": "frame8", "9": "frame9",
    "10": "frame10", "11": "frame11", "12": "frame12", "13": "frame13",
    "14": "frame14", "15": "frame15", "16": "frame16"
}

eye_ball_options = {
    "1": "ball1", "2": "ball2", "3": "ball3", "4": "ball4", "5": "ball5",
    "6": "ball6", "7": "ball7", "8": "ball8", "9": "ball9", "10": "ball10",
    "11": "ball11", "12": "ball12", "13": "ball13", "14": "ball14", "15": "ball15",
    "16": "ball16", "17": "ball17", "18": "ball18", "19": "ball19"
}

# Función para seleccionar opciones
def select_option(prompt, options):
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Elige una opción: ")
    return options.get(choice, None)

# Obtener datos de QR del usuario
def get_qr_data():
    # Selección del tipo de dato
    data_types = ["URL", "Texto Plano", "Email", "Teléfono", "SMS"]
    print("Selecciona el tipo de dato:")
    for index, option in enumerate(data_types):
        print(f"{index + 1}. {option}")
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

    # Selección de la forma del cuerpo del QR
    body = select_option("Elige la forma del cuerpo del QR:", {str(index + 1): style for index, style in enumerate(body_styles)})

    # Selección de los estilos de ojos y pupilas
    eye = select_option("Elige el estilo de los ojos del QR:", eye_options)
    eye_ball = select_option("Elige el estilo de las pupilas del QR:", eye_ball_options)

    # Selección del color del cuerpo
    print("Elige el color del cuerpo del QR:")
    color_body = input("Ingrese un color en formato hexadecimal (ej. #FF0000): ")
    
    # Selección del tamaño
    size = int(input("Ingresa el tamaño del código QR (de 100 a 1000 pixels): "))

    # Formato de descarga
    formats = {"1": "png", "2": "svg", "3": "pdf", "4": "eps"}
    format = select_option("Formato de descarga:", formats)

    # Opción de logo
    logo = None
    if input("¿Deseas agregar un logo al código QR? (si/no): ").lower() == "si":
        logo = input("Ruta del archivo del logo: ")

    return {
        "type": data_types[type_index],
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
    response = requests.post("http://localhost:3000/generate-qr", json=qr_data)
    if response.status_code == 200:
        qr_url = response.json().get('imageUrl')
        print("QR Code URL:", qr_url)
    else:
        print("Failed to generate QR code:", response.text)

if __name__ == "__main__":
    qr_data = get_qr_data()
    send_request_to_server(qr_data)
