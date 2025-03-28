# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomLoginForm, WorkerLoginForm
from django.http import HttpResponse
from .models import Client, Worker,Orders, Admin, Bar
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            client = Client.objects.filter(Phone_client=username).first()

            if client is not None:
                login(request, client)
                redirect_url = reverse('client_orders') + f'?user_id={client.id_client}'
                return redirect(redirect_url)
            else:
                return render(request, 'client_login.html', {'form': form, 'error_message': 'Пользователь с таким номером не найден'})
    else:
        form = CustomLoginForm()

    return render(request, 'client_login.html', {'form': form})

def client_orders(request):
    client_orders = Orders.objects.filter(id_client=request.GET.get("user_id"))
    context = {'client_orders': client_orders}
    return render(request, 'client_orders.html', context)

def worker_login(request):
    if request.method == 'POST':
        form = WorkerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            worker = Worker.objects.filter(mail_worker=username,Phone_Worker=password).first()
            if worker is not None:
                login(request, worker)
                redirect_url = reverse('worker_orders') + f'?user_id={worker.id_worker}'
                return redirect(redirect_url)
            else:
                return render(request, 'worker_login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = WorkerLoginForm()

    return render(request, 'worker_login.html', {'form': form})


def worker_orders(request):
    if request.method == 'POST':

        date_order = request.POST['Date_order']
        price_time = request.POST['price_time']
        id_worker = request.POST['id_worker']
        id_client = request.POST['id_client']
        id_Admin = request.POST['id_Admin']
        id_bar = request.POST['id_bar']
        worker = Worker.objects.filter(id_worker=id_worker).first()
        client = Client.objects.filter(id_client=id_client).first()
        admin = Admin.objects.filter(id_Admin=id_Admin).first()
        bar = Bar.objects.filter(id_bar=id_bar).first()

        if Orders.objects.exists():
            new_id_orders = Orders.objects.latest('id_orders').id_orders + 1
        else:
            new_id_orders = 1  # Если записей нет, создаём первый id


        order = Orders(
            id_orders=new_id_orders,
            Date_order=date_order,
            price_time=price_time,
            id_worker=worker,
            id_client=client,
            id_Admin=admin,
            id_bar=bar,
        )
        order.save()
    # Получаем заказы текущего работника
    worker_orders = Orders.objects.filter(id_worker=request.GET.get("user_id"))
    return render(request, 'worker_orders.html', {'worker_orders': worker_orders})
def update_price(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_price = request.POST.get('new_price')

        # Обновляем цену в базе данных
        order = Orders.objects.filter(id_orders=order_id).first()
        if order:
            order.price_time = new_price
            order.save()
            return HttpResponse('Цена успешно обновлена.')
        else:
            return HttpResponse('Заказ не найден.')


def search_client(request):
    if request.method == 'GET':
        search_phone_number = request.GET.get('search_phone_number')

        # Проверяем, есть ли клиент с таким номером
        client = Client.objects.filter(Phone_client=search_phone_number).first()

        if not client:
            error_message = 'Клиент с указанным телефонным номером не найден.'
            return render(request, 'search_result.html', {'error_message': error_message})

        # Получаем заказы клиента
        orders = Orders.objects.filter(id_client=client.id_client)

        context = {'client': client, 'orders': orders}
        return render(request, 'search_result.html', context)

    return render(request, 'search_result.html')







