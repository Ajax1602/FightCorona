#from selenium import webdriver
#from bs4 import BeautifulSoup
#import re
from fightCorona.servicesandrequests.models import District, Area, State

#driver = webdriver.Chrome('C:\\Users\\I331124\\Downloads\\chromedriver.exe')
fstate = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\state_unique.txt", "r")
states = [x.strip() for x in fstate.readlines()]
fstate.close()
fdist = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\districts_unique.txt", "r")
districts = fdist.readlines()
districts = [x.strip() for x in districts]
fdist.close()
farea = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\areas_unique.txt", "r")
areas = [x.strip() for x in farea.readlines()]
farea.close()
state_num = 0
dist_num = 0
area_num = 0
for state in states:
    state_num = state_num + 1
    print("state no is: "+state_num)
    stateObj = State(state_name=state.replace("_", " "))
    stateObj.save()

    for district in districts:
        dist_num = dist_num + 1
        print("district no is: "+ dist_num)
        distObj = District(distrct_name=district.split('/')[-1].replace("_", " "), state=stateObj)
        distObj.save()
        # district_name = district.district_name
        # print("district name -> " + district_name)
        #driver.get("https://bankifsccode.com/STATE_BANK_OF_INDIA/" + district)
        #print("on line: " + str(line))
        #content = driver.page_source
        #soup = BeautifulSoup(content)
        for area in areas:
            if district in area:
                area_num = area_num + 1
                print("area no is: " + area_num)
                areaObj = Area(area_name=area.split('/')[-1].replace("_"," "), district=distObj)
                areaObj.save()
