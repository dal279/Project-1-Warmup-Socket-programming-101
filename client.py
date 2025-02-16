import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port and IP address for the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # Connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # Input string from user
    message_to_server = input("Enter a string to send to the server: ")
    print("[C]: Sending to server: {}".format(message_to_server))

    # Send the string to the server
    cs.send(message_to_server.encode('utf-8'))

    # Receive the modified string from the server
    data_from_server = cs.recv(100).decode('utf-8')
    print("[C]: Received from server: {}".format(data_from_server))
    
    
    # Open the input file and send each line to the server
    with open("in-proj.txt", "r") as infile:
        for line in infile:
            # Strip newline characters and send the line
            line_to_send = line.strip()
            print("[C]: Sending to server: '{}'".format(line_to_send))
            cs.send(line_to_send.encode('utf-8'))

    # Close the client socket
    cs.close()

if __name__ == "__main__":
    client()
