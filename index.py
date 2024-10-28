from tabulate import tabulate
import clui.utils.fade as fade
import pyfiglet, os
    
def clear_console():
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
    
def fadet(text, fadetype="blackwhite"):
    fade_method = getattr(fade, fadetype, fade.blackwhite)
    return fade_method(text)
    
def align(text, space):
    for line in text.splitlines():
        print(' ' * space + line)