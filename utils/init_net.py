import socket

def get_rec_sock(ip, port):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    receive_address = (ip, port)
    send_socket.bind(receive_address)

    send_socket.listen(1)
    print("Waiting for a connection...")
    receive_socket, receive_address = send_socket.accept()
    print("Connected to:", receive_address)

    return send_socket, receive_socket

def get_send_sock(ip, port):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    send_address = (ip, port)
    print(f'Connecting to {send_address[0]}...')
    send_socket.connect(send_address)

    print('Connected.')

    return send_socket