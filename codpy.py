from Crypto.Cipher import DES
from base64 import b64encode

key = input('Ingrese una llave de 8 caracteres.\n')
if len(key) != 8:
    key = input('Llave no válida, asegúrese de que tenga 8 caracteres.\n')

msg = input('Ingrese mensaje a encriptar.\n')
msgB = bytes(msg, 'Utf-8')

cifrado = DES.new(bytes(key, 'Utf-8'), DES.MODE_CFB)
msgCifradoB = cifrado.encrypt(msgB)
iv = b64encode(cifrado.iv).decode('utf-8')
msgCifrado = b64encode(msgCifradoB).decode('utf-8')

print("iv: "+iv+" texto: "+msgCifrado)

pag = open('index.html', 'w')
pag.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js" integrity="sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    
    <p>Esta pagina contiene un mensaje secreto</p>
    <div class='DES' id='%s'></div>
    <div class='iv' id='%s'></div>
    <p id='respuesta'></p>

</body>
</html>'''% (msgCifrado, iv))

pag.close()