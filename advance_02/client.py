import queue
import socket
import sys
import threading
import click


def send_msg(sock, link):
    byte_string = str.encode(f"{link[0]}")
    sock.sendall(byte_string)


def recieve_msg(sock):
    try:
        data = sock.recv(4096)
        print(f'{data.decode("utf-8")}', file=sys.stderr)
    except:
        print("No data")


def fetch_url(sock, sem, que):
    while True:
        try:
            url = que.get()
        except que.Empty:
            continue

        if url is None:
            que.put(None)
            break

        with sem:
            try:
                send_msg(sock, url)
                recieve_msg(sock)
            except:
                print("No data")


def fetch_url_batch(sock, amount, sem, que):
    for _ in range(amount):
        fetch_url(sock, sem, que)


@click.command()
@click.option("--n-threads", "-M", type=int, default=5)
@click.option("--read-file", "-f", type=str, default="urls.txt")
def main(n_threads, read_file):
    with open(read_file) as file:
        urls = file.read().splitlines()
    amount = 100
    host = "localhost"
    port = 5_000
    sem = threading.Semaphore(n_threads)
    que = queue.Queue(maxsize=101)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print(f"Connecting to  port {server_address}", file=sys.stderr)
    sock.connect(server_address)
    threads = [
        threading.Thread(
            target=fetch_url_batch, args=(sock, amount // n_threads + 1, sem, que),
        )
        for _ in range(n_threads)
    ]
    for thread in threads:
        thread.start()
    for link in urls:
        que.put([link])
    que.put(None)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
