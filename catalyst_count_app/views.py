from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import connections
from .models import csv_data, user
from .forms import LoginForm
import pandas as pd
from . import models

@login_required
def csv_upload(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            messages.error(request, "No CSV file uploaded.")
            return render(request, 'uploadata.html')

        try:
            with connections['default'].cursor() as cursor:
                cursor.copy_expert(f"""
                    COPY {csv_data._meta.db_table}(
                        company_data, name, domain, year_founded, industry,
                        size_range, locality, country, linkedin_url,
                        current_employee_estimate, total_employee_estimate
                    )
                    FROM STDIN WITH CSV HEADER DELIMITER ','
                """, csv_file)

            messages.success(request, "CSV data uploaded successfully.")
            return redirect('uploaddata')
        except Exception as e:
            messages.error(request, f"Error while processing the CSV file: {str(e)}")

    return render(request, 'uploadata.html')

@login_required
def userdata(request):
    user1 = user.objects.all()
    return render(request, "userdata.html", {'user1': user1})

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("uploaddata"))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In successfully")
            return redirect(reverse_lazy("uploaddata"))
        else:
            messages.info(request, "Invalid credentials")
            return redirect(reverse_lazy("user_login"))
    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'login.html')

@login_required
def useradd(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        pas = request.POST.get('userpass')

        data = user(name=name, email=email, password1=pas)
        data.save()
        messages.success(request, "User Added Successfully")

        return redirect('userdata')
    return redirect('uploaddata')

from .models import csv_data

def search_csv_data(query_params):
    queryset = csv_data.objects.all()

    if 'keyword' in query_params:
        keyword = query_params['keyword']
        queryset = queryset.filter(
            models.Q(company_data__icontains=keyword) |
            models.Q(name__icontains=keyword)
        )

    if 'industry' in query_params:
        queryset = queryset.filter(industry__icontains=query_params['industry'])

    if 'year_founded' in query_params:
        queryset = queryset.filter(year_founded=query_params['year_founded'])

    if 'city' in query_params:
        queryset = queryset.filter(locality__icontains=query_params['city'])

    if 'state' in query_params:
        queryset = queryset.filter(locality__icontains=query_params['state'])

    if 'country' in query_params:
        queryset = queryset.filter(country__icontains=query_params['country'])

    if 'employee_from' in query_params:
        queryset = queryset.filter(
            total_employee_estimate__gte=query_params['employee_from']
        )

    if 'employee_to' in query_params:
        queryset = queryset.filter(
            total_employee_estimate__lte=query_params['employee_to']
        )

    results = queryset.values()
    count = queryset.count()

    return results, count

@login_required
def querybuilder(request):
    data = csv_data.objects.all().values('year_founded', 'industry', 'size_range', 'locality', 'country').distinct()

    message = ""

    if request.method == "POST":
        query_params = {
            'keyword': request.POST.get('keyword'),
            'industry': request.POST.get('industry'),
            'year_founded': request.POST.get('year_founded'),
            'city': request.POST.get('locality'),
            'state': request.POST.get('locality'),  # You mentioned 'state' and 'locality' in your previous question, so I'm assuming they both refer to 'locality'.
            'country': request.POST.get('country'),
            'employee_from': request.POST.get('employee_from'),
            'employee_to': request.POST.get('employee_to'),
        }

        filtered_data, data_count = search_csv_data(query_params)

        message = f"{data_count} data records found.\n\n"

    messages.info(request, message)

    return render(request, 'quirybuilder.html', {'data': data})

@login_required
def deletedata(request):
    data = csv_data.objects.all().delete()
    return HttpResponse("Data deleted")
