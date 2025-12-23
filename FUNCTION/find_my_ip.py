import requests
from body.speak import speak

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
    speak(ip_address)
