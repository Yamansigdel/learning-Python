import webbrowser
import sys
import pyperclip
import urllib.parse

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

encoded_address = urllib.parse.quote(address)
webbrowser.open('https://www.google.com/maps/place/' + encoded_address)

