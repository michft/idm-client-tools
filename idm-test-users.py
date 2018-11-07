#!/usr/bin/env python

# Adds and removes 10 test user accounts on the FreeIPA demo server
# Uses Python Fire library to generate a CLI for the TestUsers class
# Uses names library to generate randon user names
# Run with no arguments for usage help

import sys
import os
import fire
import names
from python_freeipa import Client, exceptions

client = Client("ipa.demo1.freeipa.org", version="2.215")
client.login("admin", "Secret123")


class TestUsers:
	def add(self):
		"""Generate and add test users to IPA and append the UIDs to a data file."""
		datafile = open('userlist.txt', 'a')
		for i in range(0, 10):
			full_name = names.get_full_name()
			username = full_name.lower().replace(" ", ".")
			first_name = full_name.split()[0]
			last_name = full_name.split()[1]
			print("Adding user: {}".format(full_name))
			client.user_add(username, first_name, last_name, full_name, disabled=True)
			datafile.write(username + "\n")

		print("\nComplete.")
		datafile.close()

	def delete(self):
		"""Parse data file for list of UIDs and delete them from IPA."""
		try:
			datafile = open('userlist.txt', 'r')
		except IOError:
			print("No data file found...exiting.")
			sys.exit()

		for user in datafile:
			try:
				print("Deleting user ID: {}".format(user), end='')
				client.user_del(user)
			except exceptions.NotFound:
				print('User not found.' + "\n")
				continue

		print("\nComplete.")
		datafile.close()
		os.remove("userlist.txt")


def main():
	fire.Fire(TestUsers)


if __name__ == '__main__':
	main()
