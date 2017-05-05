#!/usr/bin/env python3
#FDofPyNP

import socket

if __name__ == "__main__":
    hostname = 'www.baidu.com'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))