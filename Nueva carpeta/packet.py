#!/usr/bin/env python
# -*- coding: utf-8 -*-
MESSAGE = 0
PING = 1
def pack(packet_id, message):
    print("mensaje del packet "+message)
    return chr(packet_id) + message
def unpack(input_data):
    packet_id = (input_data[0] if isinstance(input_data[0], int)
                               else ord(input_data[0]))
    message = input_data[1:]
    print("mensaje en unpack dentro packet:"+message)
    return packet_id, message
def send(socket, output_data):
    try:
        socket.send(output_data)
        print("try mensaje en send dentro packet:"+output_data)
    except TypeError:
        socket.send(bytes(output_data, "utf-8"))
        print("except mensaje en send dentro packet:"+output_data)