from django.db import models

class Airport(models.Model):
    name = models.CharField("Название аэропорта", max_length=20)
    dateEst = models.CharField("Дата основания", max_length=20)
    location = models.CharField("Местоположение", max_length=40)
    workTime = models.CharField("Режим работы", max_length=100)
    airBD = models.CharField("Авиакомпании", max_length=20, null=True)

class Airline(models.Model):
    name = models.CharField("Название авиакомпании", max_length=20)
    dataAir = models.CharField("Дата основании авиакомпании", max_length=20)
    typeAir = models.CharField("Тип воздушного судна", max_length=100)
    airportID = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True)

class Route(models.Model):
    fromRoute = models.CharField("Вылет в", max_length=20)
    toRoute = models.CharField("Прилет в", max_length=20)
    dataRoute = models.CharField("Дата и время вылета", max_length=100)
    airlineID = models.ForeignKey(Airline, on_delete=models.SET_NULL, null=True)
