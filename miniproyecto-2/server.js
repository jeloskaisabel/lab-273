const net = require('net');
const https = require('https');

const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        try {
            const requestData = JSON.parse(data.toString());
            console.log('Datos recibidos:', requestData);

            // Datos de la solicitud al servidor de QR
            const qrData = JSON.stringify(requestData);

            // Configuración de la solicitud HTTPS
            const options = {
                hostname: 'api.qrcode-monkey.com',
                path: '/qr/custom',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Content-Length': qrData.length
                }
            };

            // Realizar la solicitud HTTPS
            const req = https.request(options, (res) => {
                let responseBody = '';

                // Recibir datos de la respuesta
                res.on('data', (chunk) => {
                    responseBody += chunk;
                });

                // Procesar la respuesta completa
                res.on('end', () => {
                    // Enviar la respuesta al cliente
                    socket.write(responseBody);
                    socket.end();
                });
            });

            // Manejar errores de la solicitud HTTPS
            req.on('error', (error) => {
                console.error('Error en la solicitud HTTPS:', error);
                socket.write(JSON.stringify({ error: error.message }));
                socket.end();
            });

            // Enviar datos de la solicitud al servidor de QR
            req.write(qrData);
            req.end();

        } catch (error) {
            console.error('Error al procesar la solicitud:', error);
            socket.write(JSON.stringify({ error: error.message }));
            socket.end();
        }
    });

    socket.on('error', (error) => {
        console.error('Error de socket:', error);
    });

    socket.on('close', () => {
        console.log('Conexión cerrada');
    });
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor escuchando en el puerto ${PORT}`);
});
