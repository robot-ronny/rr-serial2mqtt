# rr-serial2mqtt
serial2mqtt is a python CLI tool, that takes serial data from connected BigClown Core Module with [rr-sensor-bridge](https://github.com/robot-ronny/rr-sensor-bridge) firmware and send it via MQTT protocol on topic `sensor/<quantity>` and payload is a value from sensor.

## Install
```
git clone https://github.com/robot-ronny/rr-serial2mqtt.git
```

```
cd rr-serial2mqtt
```

```
sudo pip3 install -e .
```

## Usage
```
serial2mqtt -d <usb device path>
```

You can also specify broker host and port:
```
serial2mqtt -d /dev/ttyUSB0 -h localhsot -p 1883
```
