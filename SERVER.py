import os
import socket
import threading
import shutil

IP = socket.gethostbyname(socket.gethostname())
PORT = 4466
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_files"
client_DATA_PATH = "client_files"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "e":
            break
        elif cmd == "u":
            name = data[1]
            """
            new_base = name+'-server'
            new_name = os.path.join(SERVER_DATA_PATH, new_base)
            shutil.move(name, new_name)
            shutil.move(new_name, SERVER_DATA_PATH)
            """
            shutil.move(name, SERVER_DATA_PATH)
            send_data = "OK@File uploaded successfully."
            conn.send(send_data.encode(FORMAT))

        elif cmd == "d":
            name = data[1]
            new_base = name +'c00'
            new_name = os.path.join(client_DATA_PATH, new_base)
            shutil.move(name, new_name)
            shutil.move(new_name, client_DATA_PATH)

            send_data = "OK@File uploaded successfully."
            conn.send(send_data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def main():
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading. active_count() - 1}")

if __name__ == "__main__":
    main()