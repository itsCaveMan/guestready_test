from django.db import OperationalError
from django.shortcuts import render
from .models import Rental, Reservation
import datetime


def index(request):
    populate_database()
    return render(request, 'index.html', {'rentals': Rental.objects.all()})


def populate_database():
    try:
        Rental.objects.get(id=1)
    except OperationalError:
        ren1 = Rental.objects.create(name='rental-1')
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2022, 1, 1), checkout=datetime.date(2022, 1, 13))
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2022, 1, 20), checkout=datetime.date(2022, 2, 20))
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2022, 2, 20), checkout=datetime.date(2022, 3, 10))

        ren2 = Rental.objects.create(name='rental-2')
        Reservation.objects.create(rental=ren2, checkin=datetime.date(2022, 1, 2), checkout=datetime.date(2022, 1, 20))
        Reservation.objects.create(rental=ren2, checkin=datetime.date(2022, 1, 20), checkout=datetime.date(2022, 1, 11))
