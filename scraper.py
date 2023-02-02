import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi/")
c=r.content
soup=BeautifulSoup(c,'html.parser')
"""for i in (soup.find_all("h1")):
    print(i.text)
for i in (soup.find("p")['class']):
    print(i)"""
for i in (soup.find_all("div",class_="container")):
    print(i.get_text())
print(type(soup.title))
"""
anchors=soup.find_all("a")
s=set()
for j in anchors:
        
        s.add(j['href'])
        print(f"https://codewithharry.com{j['href']}")
"""
"""lo=soup.find("ul")
for i in (lo.children):
    print(i.text)
print(lo.parent)"""
"""
lo=soup.find("li")
for i in lo.previous_siblings:
    print(i)"""
"""lo=soup.find("ul")
print(lo.contents)
""""""

lo=soup.find("ul",id="li")
print(lo)"""
lo=soup.find("li")
with open("data.csv","w") as f:
    f.write(lo.text)   

