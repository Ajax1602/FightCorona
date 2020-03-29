from django.shortcuts import render
from django.urls import reverse_lazy
from selenium import webdriver
from bs4 import BeautifulSoup

from .forms import RequestForm
from .models import Service, SubService, Request
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


def searchservice(request):
    context = locals()
    template = 'services/services.html'
    #breakpoint()
    if request.method == "POST" and request.POST.get('search_text'):
        search_text = request.POST['search_text']
    else:
        search_text = ""
    services = Service.objects.filter(service_name__contains=search_text)

    #breakpoint()
    return render(request, template, {'services': services})


def searchsubservice(request):
    context = locals()
    template = 'subservices/subservices.html'
    if request.method == "POST" and request.POST.get('search_text'):
        search_text = request.POST['search_text']
    else:
        search_text = ""
    subservices = SubService.objects.filter(sub_service_name__contains=search_text)
    return render(request, template, {'subservices': subservices})


def searchrequest(request):
    context = locals()
    template = 'requests/requests.html'
    if request.method == "POST" and request.POST.get('subserviceid'):
        subserviceid = request.POST['subserviceid']
    else:
        subserviceid = ""
    requests = Request.objects.filter(sub_service_id=subserviceid)
    return render(request, template, {'requests': requests})


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
    # fstate = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\state_unique.txt", "r")
    # states = [x.strip() for x in fstate.readlines()]
    # fstate.close()
    # fdist = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\districts_unique.txt", "r")
    # districts = fdist.readlines()
    # districts = [x.strip() for x in districts]
    # fdist.close()
    # farea = open("C:\\Users\\I331124\\OneDrive - SAP SE\\Desktop\\my projects\\manipulation\\areas_unique.txt", "r")
    # areas = [x.strip() for x in farea.readlines()]
    # farea.close()
    # state_num = 0
    # dist_num = 0
    # area_num = 0
    # for state in states:
    #     state_num = state_num + 1
    #     print("state no is: " + str(state_num))
    #     stateObj = State(state_name=state.replace("_", " "))
    #     stateObj.save()
    #
    #     for district in districts:
    #         if state in district:
    #             dist_num = dist_num + 1
    #             print("district no is: " + str(dist_num))
    #             distObj = District(district_name=district.split('/')[-1].replace("_", " "), state=stateObj)
    #             distObj.save()
    #             # district_name = district.district_name
    #             # print("district name -> " + district_name)
    #             # driver.get("https://bankifsccode.com/STATE_BANK_OF_INDIA/" + district)
    #             # print("on line: " + str(line))
    #             # content = driver.page_source
    #             # soup = BeautifulSoup(content)
    #             for area in areas:
    #                 if district in area:
    #                     area_num = area_num + 1
    #                     print("area no is: " + str(area_num))
    #                     areaObj = Area(area_name=area.split('/')[-1].replace("_", " "), district=distObj)
    #                     areaObj.save()

    return render(request, template, context)
