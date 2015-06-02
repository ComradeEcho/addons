import math
import random
import hexchat

__module_name__ = ''
__module_author__ = 'Adie'
__module_version__ = '0'
__module_description__ = ''


 
center = 128
width = 127
frequency = .025;
# Don't touch
edited = False
 
def get_luminance(r, g, b):
    return math.sqrt(0.299 * math.pow(r, 2) + 0.587 * math.pow(g, 2) + 0.114 * math.pow(b, 2))
 
colours = ["#F0EB54","#9CB1E7","#5DF0B8","#F4A783","#A2ECEB","#F09DCB","#B4B86E","#A9EA70","#E9BA53","#9BC39A","#EEC7D8","#9AE69C","#BCCCCF","#BFC754","#65D8F3","#58C7C0","#E1B3E9","#F8A752","#4EE9EE","#B4DEC8","#81C4ED","#94CB6C","#87EAC3","#F69E96","#E9A7B9","#B8DFF4","#C9EEA8","#80E384","#E2AB70","#46EFD0","#DFD8F1","#D0DE8A","#60D592","#D3F573","#DFCC85","#BEEE8A","#57CBA1","#76F6A6","#E9E66F","#DCC75F","#C6B2CD","#75C7D5","#91C985","#A5BFD4","#C4C6F2","#9BD0CC","#8BCAB3","#62EDE0","#B6D55D","#AAEAC2"]

# def returnHex(nick):
#         random.seed(nick)
#         i = random.randint(0,255)
#         red   = random.randint(0, 255)
#         green = random.randint(0, 255)
#         blue  = random.randint(0, 255)
#         luminance = get_luminance(red, green, blue)
#         while 150 > luminance < 250:
#             red   = random.randint(0, 255)
#             green = random.randint(0, 255)
#             blue  = random.randint(0, 255)
#             luminance = get_luminance(red, green, blue)
 
#         rgb = (red, green, blue,)
#         return '#%02x%02x%02x' % rgb

def returnHex(nick):
    random.seed(nick)
    return colours[random.randint(0,len(colours)-1)]


def print_cb(word, word_eol, event, attr):
    global edited
    if edited:
        return

    msg = word[1]
    nick = hexchat.strip(word[0])

    edited = True
    try:
        prefix = word[2]
    except IndexError:
        prefix = ""
    hexchat.emit_print(event, "\003"+returnHex(nick)+nick, msg, prefix)
    edited = False

    return hexchat.EAT_ALL

hexchat.hook_print_attrs('Channel Message', print_cb, 'Channel Message', priority=hexchat.PRI_NORM)
hexchat.hook_print_attrs('Channel Action', print_cb, 'Channel Action', priority=hexchat.PRI_NORM)
hexchat.hook_print_attrs('Private Message to Dialog', print_cb, 'Channel Message', priority=hexchat.PRI_NORM)
hexchat.hook_print_attrs('Private Action to Dialog', print_cb, 'Channel Action', priority=hexchat.PRI_NORM)

