# Azure-Project-Rpi-1-Read_and_send_dht11-Rpi-2-trun_LED_when_temphighthan27

Task:- Read sensor data from a deivce(Rpi#1 with dht11) and subscribe to service bus topic and take action on Rpi#2
Steps:-
1. use 2x RaspberryPI 
2. Rpi#1: read and send the dht11 sensor data to azure hub 
3. Read that datat from azure cli #az iot hub monitor-events --hub-name kd-kd-kd --device-id my-dht11
4. Setting up your Raspberry Pi to subscribe to your Service Bus Topic
5. Trigger the LED on via using Rpi#2 Service Bus Topic


for step4:-
  4.1 Creating an Azure Service Bus Namespace and adding a Topic & Subscrition to it
  4.2 Creating Azure Stream Analytics Job
  4.3 Query editor to segregate and transform messages based on its message properties.
