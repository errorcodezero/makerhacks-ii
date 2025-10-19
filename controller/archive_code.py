# THIS IS A MOCKUP

"""
import wifi

# set access point credentials
ap_ssid = "myAP"
ap_password = "password123"

# You may also need to enable the wifi radio with wifi.radio.enabled(true)

# configure access point
wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

"""
start_ap arguments include: ssid, password, channel, authmode, and max_connections
"""

# print access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

# print IP address
print("My IP address is", wifi.radio.ipv4_address)

"""

import wifi
import socketpool

# Set access point credentials
ap_ssid = "Antifa Wireless"
ap_password = "aaaaaaaa"

# Configure access point
wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

# Print access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))
print("My IP address is", str(wifi.radio.ipv4_address_ap))

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Create a simple HTTP server function
def simple_http_server():
    server_socket = pool.socket()
    server_socket.bind((str(wifi.radio.ipv4_address_ap), 80))
    server_socket.listen(1)

    print("Server is listening on {}:80".format(wifi.radio.ipv4_address))

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from:", client_address)

        client_socket.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n")
        client_socket.send("<html>Hello, World!</html>\r\n")
        client_socket.close()

# Start the HTTP server
simple_http_server()