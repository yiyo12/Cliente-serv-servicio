#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import socket
import packet
# Compatibilidad con Python 3 
try:
    raw_input
except NameError:
    raw_input = input
def main():
    s = socket()
    s.bind(("localhost", 3030))
    s.listen(1)
    
    conn, addr = s.accept()
    
    while True:
        #mensaje recivido
        incoming_data = conn.recv(1024)
        print("mensaje recivido en incomingdata del lado servidor"+incoming_data)
        if incoming_data:
            packet_id, message = packet.unpack(incoming_data)
            
            if packet_id == packet.MESSAGE:
                packet.send(
                    conn, packet.pack(packet.MESSAGE,'servicio')#incoming_data debe recivir servicio
                    
                )
                print("incomingdata del lado ddel server"+incoming_data)
            elif packet_id == packet.PING:
                packet.send(conn, packet.pack(packet.PING, ""))
    
    s.close()
if __name__ == "__main__":
    main()
