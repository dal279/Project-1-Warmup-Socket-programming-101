import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # Receive a string from the client
    data_from_client = csockid.recv(100).decode('utf-8')
    print("[S]: Received from client: {}".format(data_from_client))

    # Reverse the string and swap its case
    modified_string = data_from_client[::-1].swapcase()
    print("[S]: Sending modified string back to client: {}".format(modified_string))

    # Send the modified string back to the client
    csockid.send(modified_string.encode('utf-8'))
    
    # Open output file for writing
    with open("out-proj.txt", "w") as outfile:
        while True:
            # Receive data from the client
            data_from_client = csockid.recv(200).decode('utf-8')

            # If no more data, break the loop
            if not data_from_client:
                break
            
            # Reverse the string and swap its case
            modified_string = data_from_client[::-1].swapcase()
            print("[S]: Received: '{}' | Modified: '{}'".format(data_from_client, modified_string))

            # Write the modified string to the output file
            outfile.write(modified_string + "\n")

    # Close the client socket and server socket
    csockid.close()
    ss.close()

if __name__ == "__main__":
    server()
