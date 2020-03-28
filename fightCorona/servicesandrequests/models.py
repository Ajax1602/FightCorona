from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=120)
    service_pic = models.ImageField(upload_to='services', blank=True)

    def __str__(self):
        return self.service_name


class SubService(models.Model):
    sub_service_id = models.AutoField(primary_key=True)
    sub_service_name = models.CharField(max_length=200)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_service_name


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    request_name = models.CharField(max_length=120)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10)
    email_address = models.EmailField(null=True, blank=True, unique=False)
    people_capacity = models.PositiveIntegerField(null=True, blank=True, unique=False)

    def __str__(self):
        return self.request_name
