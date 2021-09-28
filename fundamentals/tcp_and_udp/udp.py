import socket


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print('Connection failed')
        print(f'Error: {e}')
    else:
        print('Client Socket created successfully!')

    host = 'localhost'
    port = 5433
    message = 'Hello!\n'

    try:
        s.sendto(message.encode(), (host, 5432))
    except ValueError as e:
        print(f'Invalid port, {port}')
        print(f'Error: {e}')
    except socket.error as e:
        print(f'Impossible to connect in {host}')
        print(f'Error: {e}')
    else:
        data, server = s.recvfrom(4096)
        data = data.decode()
        print(f'Client: {data}')
    finally:
        print('Client: Closing connection...')
        s.close()


if __name__ == '__main__':
    main()
