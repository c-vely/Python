import re
import urllib.request

url = "http://google.com/googlebooks/uspto-patents-grants-text.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf8"))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for result in url_list:
    print(result)