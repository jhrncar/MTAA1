import socketserver
import socket
import sys

import proxylib


if __name__ == "__main__":
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print(ipaddress)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    proxylib.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, 5060)
    proxylib.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, 5060)

    server = socketserver.UDPServer(('0.0.0.0', 5060), proxylib.UDPHandler)
    server.serve_forever()
