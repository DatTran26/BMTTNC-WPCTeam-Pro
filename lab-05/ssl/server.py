import socket
import ssl
import threading

server_address = ("localhost", 2609)

clients = []


def handle_client(client_socket):
    clients.append(client_socket)

    print(f"Client {client_socket.getpeername()} connected.")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(
                f"Received from {client_socket.getpeername()}: {data.decode()}"
            )
            for client in clients:
                if client != client_socket:
                    try:
                        client.sendall(data)
                    except:
                        clients.remove(client)
    except:
        clients.remove(client_socket)
    finally:
        print(f"Client {client_socket.getpeername()} disconnected.")
        clients.remove(client_socket)
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print(f"Server listening on {server_address[0]}:{server_address[1]}")

while True:
    client_socket, client_address = server_socket.accept()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    context.load_cert_chain(
        certfile="certificates/server-cert.crt",
        keyfile="certificates/server-key.key",
    )

    ssl_socket = context.wrap_socket(client_socket, server_side=True)

    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()
