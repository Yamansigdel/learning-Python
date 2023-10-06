# import requests

# res=requests.get('https://sherlock-holm.es/stories/plain-text/cano.txt')
# res.raise_for_status()
# print(res.status_code)
# print(len(res.text))
# # print(res.text[:500])


# import requests,bs4

# try:
#     res = requests.get('https://sherlock-holm.es/stories/plain-text/cano.txt')
#     res.raise_for_status()
#     print(f"Status Code: {res.status_code}")
#     print(f"Response Length: {len(res.text)}")
#     print(res.text[:500])
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

# def getAmazonprice(producturl):
#     res=requests.get(producturl)
#     res.raise_for_status()
#     soup=bs4.BeautifulSoup(res.text, 'html.parser')
#     elems=soup.select('#mediaNoAccordian > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
#     return elems[0].text.strip()


# print(getAmazonprice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')) 
   
#from selenium import webdriver