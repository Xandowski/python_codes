import socket


def server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print('Connection failed')
        print(f'Error: {e}')
    else:
        print('Socket created successfully!')

    host = 'localhost'
    port = 5432

    try:
        s.bind((host, port))
    except socket.error as e:
        print('Connection failed')
        print(f'Error: {e}')
    else:
        message = 'Server: Hello client!'

    while True:
        data, address = s.recvfrom(4096)

        if data:
            print('Server sending message...')
            try:
                s.sendto(data + (message.encode()), address)
            except socket.error as e:
                print('Impossible to send message')
                print(f'Error: {e}')


if __name__ == '__main__':
    server()
