import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Connection failed')
        print(f'Error: {e}')
        sys.exit()
    else:
        print('Socket created successfully')

    host = input('Type a host or ip to connect: ')
    port = input('Type the port: ')

    try:
        s.connect((host, int(port)))
    except ValueError as e:
        print(f'Invalid port, {port}')
        print(f'Error: {e}')
    except socket.error as e:
        print(f'Impossible to connect in {host}')
        print(f'Error: {e}')
        sys.exit()
    else:
        print(f'Client TCP connected successfully to host: {host}')
    finally:
        s.shutdown(2)


if __name__ == '__main__':
    main()
