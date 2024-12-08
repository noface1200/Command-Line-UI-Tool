from tabulate import tabulate
import clui.utils.fade as fade_lib
import pyfiglet, os
    
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

ascii_fonts = pyfiglet.FigletFont.getFonts()

def data_table(data, headers='', showindex="never", tablefmt="simple"):
    working_data = [[key] + value for key, value in data.items()]
    return tabulate(working_data, headers=headers, showindex=showindex, tablefmt=tablefmt, numalign="right")
    
def ascii(text, font='slant'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art
    
def fade(text, fadetype="blackwhite"):
    fade_method = getattr(fade_lib, fadetype, fade_lib.blackwhite)
    return fade_method(text)
    
def align(text, space):
    for line in text.splitlines():
        print(' ' * space + line)
