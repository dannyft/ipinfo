#!/usr/bin/env python3

import sys
import requests

def main(argv):
    if (len(argv) == 0):
        print("Use: ipinfo <IP>")
        return

    ip = argv[0]
    response = requests.get("https://ipinfo.io/" + ip)
    info = response.json()

    length = 0
    for key, _ in info.items():
        if len(key) > length:
            length = len(key)

    for key, value in info.items():
        spaces = " " * (length - len(key))
        print(key.title() + ": " + spaces + value)

if __name__ == "__main__":
   main(sys.argv[1:])
