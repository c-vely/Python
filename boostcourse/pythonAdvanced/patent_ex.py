import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.XML", "r", encoding="utf8")as patent_xml:
    xml = patent_xml.read()

soup = BeautifulSoup(xml, "lxml")

invention_title_tag = soup.find("invention-title")
print(invention_title_tag.get_text())