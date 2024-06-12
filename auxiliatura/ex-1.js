const dgram = require('dgram');
const server = dgram.createSocket('udp4');

server.on('error', (err) => {
  console.log(`Error del servidor:\n${err.stack}`);
  server.close();
});

server.on('message', (msg, rinfo) => {
  console.log(`El servidor recibio: ${msg} de ${rinfo.address}:${rinfo.port}`);
  
  const fecha = new Date();
  const respuesta = `Fecha y hora actuales: ${fecha.toLocaleString('es-ES')}\nCliente: ${rinfo.address}:${rinfo.port}`;

  server.send(respuesta, rinfo.port, rinfo.address, (err) => {
    if (err) {
      server.close();
    }
  });
});

server.on('listening', () => {
  const address = server.address();
  console.log(`Servidor escuchando en ${address.address}:${address.port}`);
});

server.bind(7777);
