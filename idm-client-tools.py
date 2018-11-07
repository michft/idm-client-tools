#!/usr/bin/env python

# Example tasks using the lightweight FreeIPA JSON RPC client
# Uses Python Fire to generate a CLI for the ClientTools class
# Run with no arguments for usage help

import pprint
import fire
from python_freeipa import Client, exceptions

client = Client("ipa.demo1.freeipa.org", version="2.215")
client.login("admin", "Secret123")


class ClientTools:
	def usershow(self, uid):
		""" Show account details for a specified user. """
		try:
			user = client.user_show(uid)
			pprint.pprint(user)
		except exceptions.NotFound:
			print("User {} not found.".format(uid))
			exit()

	def userstatus(self, uid):
		""" Show account status for a specified user. """
		try:
			user = client.user_status(uid)
			pprint.pprint(user)
		except exceptions.NotFound:
			print("User {} not found.".format(uid))
			exit()

	def userfind(self):
		""" List all enrolled users. """
		userlist = []
		allusers = client.user_find()
		result = allusers.get('result')
		for items in result:
			userlist.extend(items.get('uid'))
		print(userlist)


def main():
	fire.Fire(ClientTools)


if __name__ == '__main__':
	main()
