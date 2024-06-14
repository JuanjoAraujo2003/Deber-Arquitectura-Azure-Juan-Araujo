import os
from azure.servicebus import ServiceBusClient, ServiceBusReceivedMessage

CONNECTION_STR = '**' # En esta linea se debe de ingresar la cadena de conexion principal para poder realizar la conexion al Azure Service Bus
QUEUE_NAME = 'colap'

def receive_messages():
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
    receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)

    with receiver:
        for msg in receiver:
            print(f"Received message: {msg.body}")
            receiver.complete_message(msg)

    servicebus_client.close()

if __name__ == '__main__':
    receive_messages()
