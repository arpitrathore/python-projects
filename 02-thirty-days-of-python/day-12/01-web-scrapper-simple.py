import requests
from requests_html import HTML

url = "https://www.boxofficemojo.com/year/world/2020"

response = requests.get(url)
print(response.status_code)
#print(response.text)

html_text = response.text

html = HTML(html = html_text, url=url)

print(html)

