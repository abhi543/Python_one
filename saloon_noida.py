from bs4 import BeautifulSoup
import requests 
from csv import writer

url="https://www.olx.in/items/q-samsung-mobiles?isSearchCall=true"
page=requests.get(url)
print(page)  

# soup=BeautifulSoup(page.content,'html.parser')

# lists=soup.find_all('div',class_="s-result-item")  

# with open('sneaker.csv','w',encoding='utf8',newline='') as f: 
#     thewriter=writer(f)
#     header=['Brand','Details', 'Rating','Price']
#     thewriter.writerow(header) 
    
    
#     for list in lists: 
#         brand=list.find('span',class_="a-size-base-plus a-color-base").text.replace('\n','')
#         details=list.find('span',class_="a-size-base-plus a-color-base a-text-normal").text.replace('\n','')
#         rating=list.find('i',class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom").text.replace('\n','')
#         price=list.find('span',class_="a-price-whole").text.replace('\n','')
#         info=[brand,details,rating,price]
#         print(thewriter.writerow(info))