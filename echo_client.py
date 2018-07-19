import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # Instantiate a TCP socket with IPv4 Addressing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)

    # Connect to the socket
    sock.connect(server_address)

    # Accumulate the entire message received back from the server
    received_message = ''
    # my_message = input("> ")
    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # Send your message to the server
        sock.sendall(my_message.encode('utf-8'))

        # Log each chunk of the message received and append to build received message
        while True:
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message += chunk

            if len(chunk) < 16:
                break

    finally:
        # close your client socket.
        print('closing socket', file=log_buffer)
        sock.close()

        # return the entire reply received from the server
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
