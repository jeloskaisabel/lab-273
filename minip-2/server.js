const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post('/generate-qr', async (req, res) => {
    const { data, body, eye, eyeBall, color_body, size, format, logo } = req.body;

    const qrConfig = {
        data: data,
        config: {
            body: body,
            eye: eye,
            eyeBall: eyeBall,
            bodyColor: color_body,
            bgColor: "#FFFFFF", // asumimos un fondo blanco por defecto
            gradientType: "linear",
            gradientOnEyes: "true", // este valor es configurable
            logo: logo
        },
        size: size,
        download: "imageUrl",
        file: format
    };

    try {
        const response = await axios.post('https://api.qrcode-monkey.com/qr/custom', qrConfig);
        res.status(200).json({ imageUrl: response.data.imageUrl });
    } catch (error) {
        console.error("Error generating QR code:", error);
        res.status(500).json({ message: "Error generating QR code" });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
