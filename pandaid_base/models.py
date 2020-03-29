from django.db import models
import django.utils.timezone as tz


# from datetime import datetime as dt


class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, )
    phone = models.CharField(max_length=15, blank=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    title = models.CharField(max_length=255, blank=False)
    location_type = models.CharField(default="", max_length=13, blank=True)
    address_1 = models.CharField(default="", max_length=255, blank=True)
    address_2 = models.CharField(default="", max_length=255, blank=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    state = models.CharField(default="", max_length=2, blank=False)
    zipcode = models.CharField(default="", max_length=10, blank=False)
    description = models.TextField(default="", blank=True)
    notes = models.TextField(default="", blank=True)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ClientNeed(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    need = models.ManyToManyField("Need")
    requested = models.DateTimeField(auto_now_add=True)
    needed = models.DateTimeField(default=tz.now, blank=False, null=False)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)


class Need(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.title


class ItemNeed(models.Model):
    need = models.ManyToManyField("Need")
    item = models.ManyToManyField("Item")
    quantity = models.IntegerField(blank=False, null=False)


class Item(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)


class ServiceNeed(models.Model):
    need = models.ManyToManyField("Need")
    service = models.ManyToManyField("Service")
    service_type = models.CharField(max_length=255, blank=False)


class Service(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.CharField(max_length=255, blank=False)


class NeedResponse(models.Model):
    client_need = models.ForeignKey("ClientNeed", on_delete=models.CASCADE)
    responder = models.ManyToManyField("Responder")
    status = models.CharField(max_length=255, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_progress_started = models.DateTimeField(default=tz.now, blank=False, null=False)
    time_completed = models.DateTimeField(default=tz.now, blank=False, null=False)


class Responder(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    job = models.CharField(max_length=255, blank=False)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE, blank=True, null=True)


class Organization(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    job = models.CharField(max_length=255, blank=False)
