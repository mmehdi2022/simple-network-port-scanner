from colorama import Fore, init
import sys
import socket


init(convert=True)

def port_scan(ip, port):
    opened = False
    for _ in range(2):
        if opened:
            print(f'{Fore.GREEN}[+]{Fore.RESET} port {port} is open.')
            return True
        try:
            sock = socket.socket()
            sock.settimeout(0.2)
            sock.connect((ip, port))
            opened = True
            sock.close()
        except:
            pass
    print(f'{Fore.RED}[-]{Fore.RESET} port {port} not open.')


def scan(ip, port_limit):
    if port_limit == 0:
        port_limit = 65525
    print(f'{Fore.CYAN}[.]{Fore.RESET}      scanning {ip} for open ports.')
    for i in range(1, port_limit+1):
        port_scan(ip=ip, port=i)
    print()

def main():
    if len(sys.argv) != 3:
        print(f'{Fore.RED}[X]{Fore.RESET} Required inputs are <target(s)> <maximum port number>.')
    else:
        target = sys.argv[1]
        limit = int(sys.argv[2])
        # target = input(f'{Fore.CYAN}[<-]{Fore.RESET} Enter target ip (separate targets with "," for multiple targets)\n{Fore.CYAN}[<-]{Fore.RESET} : ')
        # limit = int(input(f'{Fore.CYAN}[<-]{Fore.RESET} Enter the maximum ip to scan ( 0 for all known ports): '))
        if ',' in target:
            for i in target.split(','):
                scan(i.strip(), limit)
        else:
            scan(target.strip(), limit)
    

if __name__ == '__main__':
    main()
