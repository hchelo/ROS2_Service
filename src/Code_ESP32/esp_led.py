import network
import socket
from machine import Pin

# Configuración del LED
led = Pin(2, Pin.OUT)  # El LED integrado en muchas ESP32 está en el pin 2

# Conectar a la red Wi-Fi
ssid = 'ROSNET'  # Reemplaza con el nombre de tu red Wi-Fi
password = 'ROSNET2024'  # Reemplaza con tu contraseña de red

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass

    print('Conexión Wi-Fi establecida, IP:', wlan.ifconfig()[0])

# Servidor HTTP simple
def iniciar_servidor():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Escuchando en', addr)

    while True:
        cl, addr = s.accept()
        print('Cliente conectado desde', addr)
        request = cl.recv(1024)
        request = str(request)
        print('Solicitud:', request)

        if '/on' in request:
            led.value(1)
            respuesta = 'LED ENCENDIDO'
        elif '/off' in request:
            led.value(0)
            respuesta = 'LED APAGADO'
        else:
            respuesta = 'Comando desconocido'

        cl.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')
        cl.send('<html><body><h1>{}</h1></body></html>'.format(respuesta))
        cl.close()

# Conectar a Wi-Fi e iniciar el servidor
conectar_wifi()
iniciar_servidor()
