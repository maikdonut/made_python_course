import json
import logging
import socket
import threading
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
import click



def recieve_msg(connection, k, amount):
    global url_processed

    if url_processed < amount:
        try:
            data = connection.recv(4096).decode("utf-8")
            logging.debug("Data received from %s", data)

            if data != "":
                req_site = Request(data, headers={"User-Agent": "Mozilla/5.0"})
                webpage = urlopen(req_site).read()
                soup = BeautifulSoup(webpage, "html.parser")
                res = count_words(soup.get_text().strip(), k)
                send_msg = data + ":" + json.dumps(res)
                connection.sendall(send_msg.encode("utf-8"))
                url_processed += 1
                logging.debug("Number of URL: %d", url_processed)
        except:
            logging.debug("Data was not received")


def recieve_batch(connection, k, workers, amount):
    for _ in range(workers):
        recieve_msg(connection, k, amount)


def count_words(text, k):
    vectorizer = CountVectorizer()
    vect_text = vectorizer.fit_transform([text])
    vocabulary = vectorizer.get_feature_names_out()
    cnt = vect_text.toarray()[0]
    word_count = {vocabulary[i]: cnt[i] for i in range(len(vocabulary))}
    word_count_sorted = {
        key: int(value)
        for key, value in sorted(
            word_count.items(), key=lambda item: item[1], reverse=True
        )[:k]
    }

    return word_count_sorted


def handle_client_test(client):
    client.close()


def server_listen(sock, host, port, test_case=False):
    sock.setsockopt(host, port, 1)
    server_address = ("localhost", 5000)
    sock.bind(server_address)
    sock.listen(5)
    if test_case:
        client, _ = sock.accept()
        client_handler = threading.Thread(target=handle_client_test, args=(client,))
        client_handler.start()


@click.command()
@click.option("--workers", "-w", type=int, default=10)
@click.option("--top", "-k", type=int, default=5)
def main(workers, top):
    amount = 100
    sock = socket.socket()
    server_listen(sock, socket.SOL_SOCKET, socket.SO_REUSEADDR)
    logging.debug("Waiting for a connection...")
    connection, _ = sock.accept()
    threads = [
        threading.Thread(
            target=recieve_batch, args=(connection, top, amount // workers + 1, amount),
        )
        for _ in range(workers)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    sock.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    url_processed = 0
    main()
