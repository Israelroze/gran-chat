import argparse
import requests
import time

parser = argparse.ArgumentParser()
parser.add_argument('--target', default='127.0.0.1', type=str, required=False)
parser.add_argument('--port', default='5000', type=str, required=False)
parser.add_argument('--username', type=str, required=True)

MESSAGE_CACHE = []


def prompt_and_send(url, username):
    message = input("Enter your message: ")
    payload = {
        'username': username,
        'message': message
    }
    r = requests.post(url, json=payload)

    global MESSAGE_CACHE
    MESSAGE_CACHE = []
    get_and_print(url)

    #ter_status = input("Close the Session (Y/N)?")
    #return False if ter_status.lower() == 'n' else True
    return None


def get_and_print(url):
    global MESSAGE_CACHE
    res = requests.get(url)
    if len(res.json()) > len(MESSAGE_CACHE):
        for message in res.json()[len(MESSAGE_CACHE):]:
            print(f"{message['username']}:{message['message']}")
        MESSAGE_CACHE = res.json()


if __name__ == '__main__':
    args = parser.parse_args()
    server_url = f"http://{args.target}:{args.port}/chat"
    #terminate = False
    while True:
        try:
            get_and_print(server_url)
            time.sleep(1)
        except KeyboardInterrupt:
            terminate = prompt_and_send(server_url, args.username)
