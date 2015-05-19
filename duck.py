import hexchat
import re
from random import randint

__module_name__ = 'DuckHunt'
__module_author__ = 'Cassie Swanson'
__module_version__ = '0'
__module_description__ = '.bef ducks!'

def _cb(word, word_eol, userdata):
	if hexchat.strip(word[0]) in ["gonzobot"]:
		duckDetect = re.search("o<|o​<", hexchat.strip(word[1]))
		if duckDetect is not None:
			print("quack")
			context = hexchat.get_context()	
			hexchat.hook_timer(randint(3000,7000), duck, context)

def duck(context):
	command = "msg " + context.get_info("channel") + " .bef"
	context.command(command)




def unload_cb(userdata):
	print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_print('Channel Message', _cb)
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')