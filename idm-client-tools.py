#!/usr/bin/env python

import sys
import pprint
import fire
from python_freeipa import Client, exceptions


""" Example tasks using the lightweight FreeIPA JSON RPC client"""
""" Uses Python Fire to generate a CLI for the ClientTools class """


client = Client("ipa.demo1.freeipa.org", version="2.215")
client.login("admin", "Secret123")


class ClientTools:
    def usershow(self, uid):
        try:
            user = client.user_show(uid)
            pp = pprint.pformat(user)
            sys.stdout.write(pp)
            sys.stdout.flush()
        except exceptions.NotFound:
            print("User {} not found.".format(uid))
            exit()

    def userstatus(self, uid):
        try:
            user = client.user_status(uid)
            pp = pprint.pformat(user)
            sys.stdout.write(pp)
            sys.stdout.flush()
        except exceptions.NotFound:
            print("User {} not found.".format(uid))
            exit()


def main():
    fire.Fire(ClientTools)


if __name__ == '__main__':
    main()
