from kafka import KafkaConsumer
from json import loads
from tower_jsnapy_all import send_request
import re


def kafka_cleanup(each_message):
    host_ip = each_message.value['host']
    host_name = each_message.value['hostname']
    msg = each_message.value['router_message']
    return(host_ip, host_name, msg)


def syslog_cleanup(msg):
    match = re.match(r"^\[(?P<junos_string>.*)]", msg)
    if match:
        junos_string = match.groupdict(['junos_string'])
        for k, v in junos_string.items():
            msg = v.split(" ")
            neighbor = msg[1]
            neighbor = neighbor.split("=")
            neighbor = neighbor[1].replace('"','')
        return(neighbor)


route_reflectors = ["139.65.224.11", "10.255.0.2"]


consumer = KafkaConsumer(
   'bgp_down',
    enable_auto_commit=True,
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['kafka_server:9092']
    )

for each_message in consumer:
    host_ip, host_name, msg = kafka_cleanup(each_message)
    neighbor = syslog_cleanup(msg)
    print("host_ip: {}, host_name: {}, neighbor: {}".format(host_ip, host_name, neighbor))
    x = send_request()
    print(x)
    if neighbor in route_reflectors:
        print("yep:\n{}".format(neighbor))
    else:
        print("nope:\n{}".format(neighbor))
