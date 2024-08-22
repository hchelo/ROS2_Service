import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import requests

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        # Interpretar el valor de `a`
        if request.a == 1:
            response.sum = 1  # Mensaje de "encendido"
            url = "http://192.168.107.43/on"
            self.send_request(url)
        elif request.a == 0:
            response.sum = 0  # Mensaje de "apagado"
            url = "http://192.168.107.43/off"
            self.send_request(url)
        else:
            response.sum = -1  # Mensaje de error o valor no reconocido

        self.get_logger().info('Incoming request: a: %d' % request.a)
        return response

    def send_request(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.get_logger().info('Solicitud HTTP exitosa: %s' % response.text)
            else:
                self.get_logger().info('Error en la solicitud HTTP: Código %d' % response.status_code)
        except requests.RequestException as e:
            self.get_logger().error('Excepción en la solicitud HTTP: %s' % str(e))

def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
