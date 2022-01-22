from bs4 import BeautifulSoup
import requests 
from csv import writer

url="https://www.amazon.in/s?k=sneakers+for+men&s=date-desc-rank&crid=8G0LY32IYMW9&qid=1642413282&sprefix=sneakers%2Caps%2C372&ref=sr_st_date-desc-rank"
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