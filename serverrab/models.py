# models.py

from django.db import models

class Admin(models.Model):
    id_Admin = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=120, null=True)
    Phone_Admins = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    mail_admins = models.CharField(max_length=120, null=True)
    naznach_Admins = models.DateField(null=True)

    class Meta:
        db_table='admin'

    def __str__(self):
        return self.FIO

class Worker(models.Model):
    id_worker = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=120, null=True)
    Phone_Worker = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    mail_worker = models.CharField(max_length=20, null=True)
    naznach_Worker = models.DateField(null=True)
    last_login = models.DateTimeField(null=True)

    class Meta:
        db_table='worker'
    def __str__(self):
        return self.FIO

class Client(models.Model):
    id_client = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    Phone_client = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    last_login = models.DateTimeField(null=True)
    class Meta:
        db_table='client'

    def __str__(self):
        return f"{self.name} - {self.Phone_client}"
class Pristavka(models.Model):
    id_pristav = models.IntegerField(primary_key=True)
    nazvanie = models.CharField(max_length=20, null=True)
    price_pristavka = models.IntegerField(null=True)
    game = models.CharField(max_length=20, null=True)
    class Meta:
        db_table='pristavka'

    def __str__(self):
        return f"Pristavka ID: {self.id_pristav}"


class Computers(models.Model):
    id_computers = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20, null=True)
    password = models.IntegerField(null=True)
    device = models.CharField(max_length=20, null=True)
    class Meta:
        db_table='computers'

    def __str__(self):
        return f"Computers ID: {self.id_computers}"

class Bar(models.Model):
    id_bar = models.IntegerField(primary_key=True)
    price_bar = models.IntegerField(null=True)
    class Meta:
        db_table='bar'

    def __str__(self):
        return f"Bar ID: {self.id_bar}"
class Rooms(models.Model):
    id_rooms = models.IntegerField(primary_key=True)
    vip = models.BooleanField(null=True)
    price_rooms = models.IntegerField(null=True)
    id_computers = models.ForeignKey(Computers, on_delete=models.CASCADE, db_column='id_computers')
    id_pristav = models.ForeignKey(Pristavka, on_delete=models.CASCADE,db_column='id_pristav')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE,db_column='id_client')
    class Meta:
        db_table='rooms'

    def __str__(self):
        return f"Room ID: {self.id_rooms}"
class Orders(models.Model):
    id_orders = models.IntegerField(primary_key=True)
    Date_order = models.DateField(null=True)
    price_time = models.IntegerField(null=True)
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE,db_column='id_worker')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE,db_column='id_client')
    id_Admin = models.ForeignKey(Admin, on_delete=models.CASCADE,db_column='id_Admin')
    id_bar = models.ForeignKey(Bar, on_delete=models.CASCADE, null=True,db_column='id_bar')
    class Meta:
        db_table='orders'

    def __str__(self):
        return f"Order ID: {self.id_orders}"

class CompClub(models.Model):
    id_compclube = models.IntegerField(primary_key=True)
    id_Admin = models.ForeignKey(Admin, on_delete=models.CASCADE,db_column='id_Admin')
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE,db_column='id_worker')
    id_rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE,db_column='id_rooms')
    id_computers = models.ForeignKey(Computers, on_delete=models.CASCADE,db_column='id_computers')
    id_pristav = models.ForeignKey(Pristavka, on_delete=models.CASCADE,db_column='id_pristav')
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE,db_column='id_client')
    id_orders = models.ForeignKey(Orders, on_delete=models.CASCADE,db_column='id_orders')
    name = models.CharField(max_length=20, null=True)
    class Meta:
        db_table='compclube'

    def __str__(self):
        return f"{self.id_compclube} - {self.name}"
