'''from bs4 import BeautifulSoup
import requests 

url="https://program.goteborgfilmfestival.se/en/digitalfilm"
page=requests.get(url)
#print(page)
soup=BeautifulSoup(page.content,'html.parser')

lists=soup.find_all('div',class_="movie-grid")

for list in lists: 
    title=list.find('div',class_="data-v-559b8970")
    info=[title]
    print(info)'''
    
import requests 
from bs4 import BeautifulSoup 
url="https://codewithharry.com" 
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

title=soup.title 
#print(title)
paras=soup.find_all('p')
#print(paras)

anchors=soup.find_all('a')
#print(anchors)
#print(soup.find('p'))['class']#print 1st line
#print(soup.find_all("p",class_="lead"))
print(soup.get_text())# all texts

anchors=soup.find_all('a')
all_links=set()
for link in anchors:
    if(link.get('href') !='#'):
        linkText="https://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText) 