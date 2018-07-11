import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # instantiate a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # bind socket to the address above and begin to listen
    sock.bind(address)
    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # make a new socket when a client connects, called'conn',
            conn, addr = sock.accept()

            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # receive 16 bytes of data from the client
                    buffer_size = 16
                    data = conn.recv(buffer_size)

                    print('received "{0}"'.format(data.decode('utf8')))
                    
                    # Send the data you received back to the client and print confirmation
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))
                    
                    # Check to see whether you have received the end of the message
                    if len(data) < 16:
                        break

            finally:
                # Close the socket created when the client connected.
                sock.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # KeyboardInterrupt closes the server socket and concludes the server function.
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
