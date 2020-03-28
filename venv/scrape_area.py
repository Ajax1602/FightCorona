from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome('C:\\Users\\I331124\\Downloads\\chromedriver.exe')
fread = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\districts_unique.txt", "r")
districts = fread.readlines()
districts = [x.strip() for x in districts]
fread.close()
fwrite = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\areas.txt", "w",
              encoding="utf-8")
line = 0
for district in districts:
    line = line + 1
    # district_name = district.district_name
    # print("district name -> " + district_name)
    driver.get("https://bankifsccode.com/STATE_BANK_OF_INDIA/" + district)
    print("on line: " + str(line))
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a', href=re.compile("bankifsccode.com/STATE_BANK_OF_INDIA/" + district)):
        name = a['href']
        print("name is " + name)
        fwrite.write(name + "\n")

fwrite.close()
