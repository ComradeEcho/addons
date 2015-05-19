# stutter.py
# by Adie
from random import randint
import hexchat
__module_name__ = 'Stutter'
__module_author__ = 'Adie'
__module_version__ = '0'
__module_description__ = 'Returns a string with a possible chance of some words being stuttered.'
 
# Frequency per word, out of 100.
FREQ = hexchat.get_pluginpref("stutter_freq")

 
# Returns a string with a possible chance of some words being stuttered.
#        return ' '.join(map(lambda s: ('%s-%s' % (s[0], s[0].lower() + s[1:])) if FREQ >= randint(0, 100) else s, text.split(' '))) if len(text) > 0 else text


def stutter(text):
    x = ''
    input = text.split()
    for i in input:
        if i.isalpha() and FREQ >= randint(0, 100) and len(i) > 2:
            x = x + ('%s-%s' % (i[0], i[0] + i[1:])) + ' '
        else:
            x = x + i + ' '
    return x
    

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
    hexchat.command("settext %s" % stutter(msg))
    
def change_freq(word, word_eol, userdata):
    hexchat.set_pluginpref("stutter_freq", word[1])
    FREQ = hexchat.get_pluginpref("stutter_freq")
    hexchat.prnt("Stutter frequency set to " + str(FREQ))


	
hexchat.hook_print('Key Press', send_message)
hexchat.hook_command("freq", change_freq)
print("\00304", __module_name__, "successfully loaded.\003")
 
# Example usage:
# print stutter('Man, I think next month i\'m go get myself like $100 worth of heroin and just have myself a good month')