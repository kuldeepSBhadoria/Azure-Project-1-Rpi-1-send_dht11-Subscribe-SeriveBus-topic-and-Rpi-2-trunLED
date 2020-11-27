import json
import RPi.GPIO as GPIO
#from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
from azure.servicebus import ServiceBusClient, ServiceBusMessage

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_LED = 4
GPIO.setup(PIN_LED, GPIO.OUT)


CONNECTION_STR = "Endpoint=sb://myservice-busnamespace.servicebus.windows.net/;SharedAccessKeyName=TriggerActionPolicy;SharedAccessKey=MRZCHjHFgmtashT8I0C7NgATJtsQW5r+S4AN0hbk2/c="
TOPIC_NAME = "mytemperaturetopic"
SUBSCRIPTION_NAME = "mytemptopic"

while True:
    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR)
    with servicebus_client:
        receiver = servicebus_client.get_subscription_receiver(
            topic_name=TOPIC_NAME,
            subscription_name=SUBSCRIPTION_NAME
        )
        with receiver:
            received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
            for msg in received_msgs:
               print(str(msg))
               receiver.complete_message(msg)
               if('1' in str(msg)):
                   print("1 LED ON")
                   GPIO.output(PIN_LED, True)

               if('0' in str(msg)):
                   print("0 LED off")
                   GPIO.output(PIN_LED, False)
