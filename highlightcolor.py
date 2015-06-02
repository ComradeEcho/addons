import hexchat

__module_name__ = 'PM Highlight'
__module_author__ = 'Adie'
__module_version__ = '0'
__module_description__ = 'Makes PMs the highlight colour rather than channel message colour'

def isPM(word, word_eol, userdata):
    hexchat.command('gui color 3')

hexchat.hook_print("Private Message to Dialog", isPM)
hexchat.hook_print("Private Action to Dialog", isPM)
