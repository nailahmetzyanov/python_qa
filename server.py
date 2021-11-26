import socket
import re

HOST = "127.0.0.1"
PORT = 14444


def parse_request_method(get_data: str):
    regexp = r'^[A-Z]{1,10}'
    req_list = re.findall(regexp, get_data)
    return req_list[0]


def parse_headers(get_data: str):
    lines = get_data.split('\n')
    i = 1
    headers_list = []
    while i < len(lines):
        headers_list.append(lines[i])
        i += 1
    return headers_list


def parse_status(get_data: str):
    lines = get_data.split('\n')
    status = lines[0].split(" ")[1]
    search_status = re.search(r"(\/\?status=)(\d{1,3})$", status)
    if search_status is None:
        return '200 OK'
    status = int(search_status.group(2))
    if status == 500:
        return '500 INTERNAL_SERVER_ERROR'
    elif status == 400:
        return '400 BAD_REQUEST'
    elif status == 404:
        return '404 NOT FOUND'
    elif status == 300:
        return '300 MULTIPLE_CHOICES'
    elif status == 200:
        return '200 OK'
    elif status == 100:
        return '100 CONTINUE'
    else:
        return '200 OK'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    print(f"[STARTING] Server is listening on {HOST}:{PORT}")
    server.bind((HOST, PORT))
    server.listen()
    while True:
        conn, addr = server.accept()
        print(f"[INFO] Got connection from client {addr} / {conn}")
        with conn:
            while True:
                data_recvd = conn.recv(1024).decode("utf-8")
                print("[WORKING] Received", "from", addr)
                if not data_recvd or data_recvd == b"close":
                    print("[INFO] Got termination signal", data_recvd, "and closed connection")
                    conn.close()
                print(type(parse_request_method(data_recvd)))
                data = f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html>' \
                       f'<body>' \
                       f'Request Method: {parse_request_method(data_recvd)}' '<br>' \
                       f'Request Source: {addr}' '<br>' \
                       f'Request Status: {parse_status(data_recvd)}' '<br>' \
                       f'{parse_headers(data_recvd)}<br>' \
                       f'</body></html>\n'
                conn.send(data.encode("ascii"))
                conn.shutdown(socket.SHUT_RDWR)
                break
