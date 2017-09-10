# echoasyncio.py

from socket import socket, AF_INET, SOCK_STREAM
import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def echo_client(sock):
    while True:
        data = yield from loop.sock_recv(sock, 8192)
        if not data:
            break
        yield from loop.sock_sendall(sock, data)
    sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    while True:
        client_sock, addr = yield from loop.sock_accept(sock)
        asyncio.async(echo_client(client_sock))
        
if __name__ == '__main__':
    asyncio.async(echo_server(('',25000)))
    loop.run_forever()
    
