import sys
import click
import serial
import paho.mqtt.client as mqtt


@click.command()
@click.option("--device", "-d", help="Device path",
              type=click.Path(exists=True), required=True)
@click.option("--host", "-h", help="MQTT host", default="localhost")
@click.option("--port", "-p", help="MQTT host port", default=1883)
def main(device, host, port):
    serialport = serial.Serial(port=device, baudrate=115200,
                               bytesize=8, stopbits=serial.STOPBITS_ONE)

    mqttc = mqtt.Client()
    mqttc.connect(host, port)

    while True:
        data = str(serialport.readline(), "utf-8").replace("\n", "").split()
        topic = data[0][2:-2]
        payload = data[1][:-1]
        mqttc.publish("sensor/ronny/{0}".format(topic.split("/")[3]), payload)
        print("topic: {0}, payload: {1}".format(topic, payload))
