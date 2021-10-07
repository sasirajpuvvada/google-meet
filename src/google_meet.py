import webbrowser
from string import ascii_uppercase, ascii_lowercase
from random import randint

MEET_URL = "https://g.co/meet/"
CHARS = ascii_lowercase + ascii_uppercase

def generate_url():
    end_point = ""
    
    for _ in range(7):
        end_point += CHARS[randint(0,len(CHARS)-1)]
    return MEET_URL + end_point


url = generate_url()
webbrowser.open(url)