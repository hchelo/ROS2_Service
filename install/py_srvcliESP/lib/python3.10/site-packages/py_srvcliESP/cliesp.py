import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalClient(Node):

    def __init__(self):
        super().__init__('minimal_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servicio no disponible, esperando...')

        self.req = AddTwoInts.Request()

    def send_request(self, value):
        self.req.a = value
        self.req.b = 0  # `b` no se usa, pero debe ser proporcionado
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClient()

    if len(sys.argv) < 2:
        minimal_client.get_logger().error('Por favor, proporciona un valor (0 o 1) como argumento.')
        return

    try:
        value_to_send = int(sys.argv[1])
        if value_to_send not in [0, 1]:
            minimal_client.get_logger().error('El valor debe ser 0 o 1.')
            return
    except ValueError:
        minimal_client.get_logger().error('El valor proporcionado no es un número entero válido.')
        return

    response = minimal_client.send_request(value_to_send)

    if response:
        if response.sum == 1:
            minimal_client.get_logger().info('Respuesta recibida: Encendido')
        elif response.sum == 0:
            minimal_client.get_logger().info('Respuesta recibida: Apagado')
        else:
            minimal_client.get_logger().info('Respuesta recibida: Valor no reconocido')
    else:
        minimal_client.get_logger().info('No se recibió respuesta del servicio.')

    rclpy.shutdown()

if __name__ == '__main__':
    main()
