import requests
from bs4 import BeautifulSoup

products_to_track = [

    {

        "product_url": "https://www.amazon.in/Samsung-Galaxy-Prime-Space-Storage/dp/B085J1D8BH/ref=sr_1_1_sspa?dchild=1&keywords=m31&qid=1612441951&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOVdKOE81Nk1JTlFRJmVuY3J5cHRlZElkPUEwMDQ5NDc1MkM1VlU0MDdDTVFHSiZlbmNyeXB0ZWRBZElkPUEwMjk4MjA2MUJVUlBSUllKOTY1RSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "Samsung M31",
        "target_price": 16000
    },

    {
        "product_url": "https://www.amazon.in/dp/B07HGH88GL/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=9lwNOxSV1nCtzIm5bbugfg&hsa_cr_id=6755663130002&pd_rd_plhdr=t&pd_rd_r=db9ee914-a095-43a7-a985-513c2e39f30e&pd_rd_w=LE21X&pd_rd_wg=mpQyj&ref_=sbx_be_s_sparkle_mcd_asin_1_img",
        "name": "Samsung M21 6GB 128",
        "target_price": 16000
    },

    {
        "product_url": "https://www.amazon.in/Redmi-Note-Pro-Champagne-Storage/dp/B08696XB45/ref=sr_1_10?crid=LPHHW4C5XFF2&dchild=1&keywords=redmi+note+9+pro&qid=1612449844&s=electronics&sprefix=redmi+%2Celectronics%2C344&sr=1-10",
        "name": "RedmiNote 9 Pro",
        "target_price": 13000
    },
    {
        "product_url": "https://www.amazon.in/Apple-iPhone-8-Red-64GB/dp/B07CGHYKKB/ref=sr_1_4?crid=9MNN6C50H7QR&dchild=1&keywords=iphone+8&qid=1612465156&sprefix=Iphone%2Caps%2C339&sr=8-4",
        "name": "iPhone 8 64GB",
        "target_price": 63000
    },
    {
        "product_url": "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5WG761/ref=sr_1_1_sspa?crid=3RQZ18JZRJ0GU&dchild=1&keywords=macbook+pro&qid=1612465340&sprefix=Mac%2Caps%2C336&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUzZJMUpYTFk2NU42JmVuY3J5cHRlZElkPUEwNjAyNjI0QkY2Qk9XQTFFNkFUJmVuY3J5cHRlZEFkSWQ9QTA3MDYyNDZOOUFaMDRIT1hKVUcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
        "name": "New Apple MacBook Pro",
        "target_price": 1239000
        }

]


def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify()) #prassing the data in html format
    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()


result_file = open('my_result.txt', 'w')

try:

    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(
                every_product.get("name") + '-\t' + 'Availale at Target Price ' + 'Current Price -' + str(
                    my_product_price) + '\n')

        else:
            print("Still at current price")
finally:
    result_file.close()
