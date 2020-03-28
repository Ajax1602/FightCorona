from django.shortcuts import render
from django.urls import reverse_lazy
from selenium import webdriver
from bs4 import BeautifulSoup

from .forms import RequestForm
from .models import State, District, Area
from django.views.generic import FormView
import re


# Create your views here.
def request_create_view(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
    #breakpoint()
    context = {
        'form': form
    }
    return render(request, "requests/requestformnew.html", context)


def search(request):
    context = locals()
    template = 'search.html'
    return render(request, template, context)


def requestform(request):
    context = locals()
    template = 'requests/requestform.html'
    return render(request, template, context)


def requestdetail(request):
    context = locals()
    template = 'requests/requestdetails.html'
    return render(request, template, context)


def test(request):
    context = locals()
    template = 'test.html'
    driver = webdriver.Chrome('C:\\Users\\I331124\\Downloads\\chromedriver.exe')
    f = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\districts.txt", "w")
    for district in District.objects.all():
        district_name = district.district_name
        print("district name -> " + district_name)
        #driver.get("https://bankifsccode.com/STATE_BANK_OF_INDIA/"+district.state.state_name+"/"+district_name)
        #content = driver.page_source
        #soup = BeautifulSoup(content)
        # for a in soup.findAll('a', href=re.compile("bankifsccode.com/STATE_BANK_OF_INDIA/"+district.state.state_name+"/"+district_name)):
        #     name = a['href'].rsplit('/', 1)[-1]
        #     Area(area_name=name, district=district).save()
        #     print("name is " + name)
        f.write(district.state.state_name+"/"+district_name+"\n")
    f.close()
    return render(request, template, context)
