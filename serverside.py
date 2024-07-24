import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection from {client_address} closed")
            break
        
        print(f"Received message from {client_address}: {message}")
        
        # Broadcast message to all clients
        broadcast(message, client_socket)
    
    # Close client socket
    client_socket.close()

# Function to broadcast message to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                # Remove broken socket
                clients.remove(client)

# Main function
def main():
    # Initialize server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    
    print("Server listening on port 9999...")
    
    while True:
        # Accept incoming connections
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        
        # Handle client in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# List to store client sockets
clients = []

if __name__ == "__main__":
    main()
