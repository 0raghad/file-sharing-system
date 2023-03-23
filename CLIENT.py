import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "e":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("Enter D for download or U for upload or e to exit: ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "u":
           # data[1]= input('Enter file name: ')
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            """
            path = data[1] = input('Enter file name: ')
            filename = path.split("/")[-1]
            send_data = f"{cmd}@{path}"
            client.send(send_data.encode(FORMAT))
            """

        elif cmd == "d":
            filename = input('Enter file name:\n')
            client.send(f"{cmd}@{filename}".encode(FORMAT))

    print("Disconnected from the server.")
    client.close()


if __name__ == "__main__":
    main()