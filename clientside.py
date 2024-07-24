import socket
import threading

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode()
            print("\n" + message)
        except:
            # If an error occurs, close the connection
            print("An error occurred. Exiting...")
            client_socket.close()
            break

# Main function
def main():
    # Initialize client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    
    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        # Send message to server
        message = input()
        client.send(message.encode())

# Run the main function
if __name__ == "__main__":
    main()
