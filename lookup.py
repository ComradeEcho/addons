import os
os.chdir(r"C:\Users\Adie\AppData\Roaming\HexChat\addons")
import hexchat
import iplookup
from re import search
import socket



__module_name__ = ''
__module_author__ = 'TingPing'
__module_version__ = '0'
__module_description__ = ''


def _cb(word, word_eol, userdata):
	if hexchat.get_info("network") in ["UnderNet", "DALnet"]:
		if hexchat.get_info("channel")[:1] is not "#":
			try:
				result = search(".+@(.+)", hexchat.get_info("topic"))
			except Exception as e:
				print("Error: " + e + ', hexchat.get_info("topic") = ' + hexchat.get_info("topic"))

			if result is not None:
				hostname = result.group(1)
				try:
					host = socket.gethostbyname(hostname)
					bob = iplookup.userLookup(host)
					hexchat.command("msg %s Your IP %s resolves to %s" % (hexchat.get_info("channel"), host, bob.location))
				except Exception as e:
					print(e)


def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_print('Open Context', _cb)
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')