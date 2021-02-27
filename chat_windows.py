import socket
import threading
import os

af = socket.AF_INET  # Ipv4 address family
protocol = socket.SOCK_DGRAM # UDP protocol

my_sock = socket.socket(af, protocol)

ip = ""
port = 1234

my_sock.bind((ip, port))

all_msgs = []

def print_msgs():
    os.system("cls")
    for msg in all_msgs:
        print(f"{msg['sender']}: {msg['message']}")
    print()

def send_msg():
    port = 1234
    print("Enter IP:")
    ip = input()
    while True:
        msg = input("Message:\n")
        my_sock.sendto(msg.encode(), (ip, port))
        all_msgs.append({"message": f"{msg}", "sender": "Me", "port": f"{port}"})
        print_msgs()

send_thread = threading.Thread(target=send_msg)
send_thread.start()

def recv_msg():
    while True:
        data = my_sock.recvfrom(4096)
        msg = data[0].decode()
        sender = data[1][0]
        all_msgs.append({"message": f"{msg}", "sender": f"{sender}", "port": f"{data[1][1]}"})
        print_msgs()        

recv_msg()