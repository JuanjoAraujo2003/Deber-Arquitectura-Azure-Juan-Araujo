import os
from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = '***' # En esta linea se debe de ingresar la cadena de conexion principal para poder realizar la conexion al Azure Service Bus
QUEUE_NAME = 'colap'

def send_messages():
    alerts = [
        "Alerta del servidor 1: Uso de CPU por encima del 90%",
        "Alerta del servidor 2: Uso de memoria por encima del 85%",
        "Alerta del servidor 3: Espacio en disco por debajo del 10%",
        "Alerta del servidor 4: Latencia de red por encima de 200ms",
        "Alerta del servidor 5: Alto número de errores 500",
        "Alerta del servidor 6: El pool de conexiones de la base de datos está agotado",
        "Alerta del servidor 7: Tiempo de respuesta del servidor de aplicaciones lento",
        "Alerta del servidor 8: Intentos de inicio de sesión no autorizados detectados",
        "Alerta del servidor 9: Alta temperatura de CPU detectada",
        "Alerta del servidor 10: Problema de suministro de energía detectado",
        "Alerta del servidor 11: Fallo en el proceso de respaldo",
        "Alerta del servidor 12: Intento de violación del firewall",
        "Alerta del servidor 13: El servidor DNS no responde",
        "Alerta del servidor 14: La cola del servidor de correo está llena",
        "Alerta del servidor 15: El servicio XYZ no está en ejecución"
    ]

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)

    with sender:
        for alert in alerts:
            message = ServiceBusMessage(alert)
            sender.send_messages(message)
            print(f"Sent message to the queue: {alert}")

    servicebus_client.close()

if __name__ == '__main__':
    send_messages()
