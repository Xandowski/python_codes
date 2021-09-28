import os


def readInput():
    ip = input("Digite o ip ou host: ")
    os.system(f'ping -c 6 {ip}')


def readFile():
    with open('hosts.txt', 'r') as file:
        ips = file.read().split('\n')
        for ip in ips:
            os.system(f'ping -c 3 {ip}')


readFile()
