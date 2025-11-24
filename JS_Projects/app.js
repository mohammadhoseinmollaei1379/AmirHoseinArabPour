const qr = require('qrcode')

qr.toFile('qrcode.png', 'https://www.instagram.com/dahoo_mes/', {width: 1200})