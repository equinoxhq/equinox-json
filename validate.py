#!/usr/bin/env python3
import json

if __name__ == '__main__':
    try:
        file = json.load(open("equinox.json", "r"))
        print("This file is fine.")
    except json.decoder.JSONDecodeError as exc:
        print("This file isn't fine: ", exc)
