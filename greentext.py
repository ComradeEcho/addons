import hexchat
import re
__module_name__ = 'Greentext'
__module_author__ = 'Adie'
__module_version__ = '0'
__module_description__ = 'Turns text green if it starts with ">"'
 

def greentext(text):
    result = re.search("\A>[^\W_].+", text)
    if result is not None:
    	return "\0033"+text
    else:
    	return text
   
 
def send_message(word, word_eol, userdata):
    """ Gets the inputbox's text, perform substitutions and replaces it.
   
   This function is called every time a key is pressed. It will stop if that
   key isn't ENTER (without modifiers, e.g. SHIFT + ENTER), or if the input
   box is empty.
   
   """
    if not(word[0] == "65293" and word[1] == "0"):
        return
    msg = hexchat.get_info('inputbox')
    if msg is None:
            return
    hexchat.command("settext %s" % greentext(msg))

def receive_message(word, word_eol, userdata):
	result = re.search("\A>[^\W_].+", word[1])
	if result is not None:
		hexchat.emit_print("Channel Message", word[0], "\0033"+word[1], word[2], word[3])
		return hexchat.EAT_ALL
	else:
		return hexchat.EAT_NONE


       
hexchat.hook_print('Key Press', send_message)
hexchat.hook_print("Channel Message", receive_message)
print("\00304", __module_name__, "successfully loaded.\003")
 
