import sys
import requests
from datetime import datetime

from format import format_msg

def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website)
    # send the message
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error"

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    website = None
    if len(sys.argv) > 1:
        name = sys.argv[1]
    if len(sys.argv) > 1:
        website = sys.argv[2]
    response = send(name, website=website, verbose=True)
    print(response)