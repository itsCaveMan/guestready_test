from django.test import TestCase
import datetime
from guestready_test.models import Rental, Reservation


class ReservationClass(TestCase):
    """
    Test cases for the 'previous_reservation' property on the Reservations model
    """

    def setUp(self):
        ren1 = Rental.objects.create(name='rental-1')
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2000, 1, 1), checkout=datetime.date(2000, 1, 2))
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2000, 1, 3), checkout=datetime.date(2000, 1, 4))

        Reservation.objects.create(rental=ren1, checkin=datetime.date(2000, 2, 5), checkout=datetime.date(2000, 2, 10))
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2000, 2, 1), checkout=datetime.date(2000, 2, 4))
        Reservation.objects.create(rental=ren1, checkin=datetime.date(2000, 2, 11), checkout=datetime.date(2000, 2, 20))

        ren2 = Rental.objects.create(name='rental-2')
        Reservation.objects.create(rental=ren2, checkin=datetime.date(2000, 1, 1), checkout=datetime.date(2000, 1, 2))
        Reservation.objects.create(rental=ren2, checkin=datetime.date(2000, 1, 3), checkout=datetime.date(2000, 1, 4))

    def test_previous_reservation_simple(self):
        """ test a simple 'next day/previous day' reservation setup """
        res2 = Reservation.objects.get(id=2)
        res1 = res2.previous_reservation
        self.assertTrue(res1.id == 1, 'the previous reservation is incorrect')

    def test_previous_reservation_complex(self):
        """ test a complex reservation setup
            where the row order does not follow the reservation chronological order """
        res5 = Reservation.objects.get(id=5)
        res4 = res5.previous_reservation
        self.assertTrue(res4.id == 3)

        res4 = Reservation.objects.get(id=3)
        res3 = res4.previous_reservation
        self.assertTrue(res3.id == 4)

    def test_previous_reservation_rentals(self):
        """ test that the previous reservation property is not returning itself """
        res2 = Reservation.objects.get(id=1)
        res7 = Reservation.objects.get(id=7)
        self.assertEquals(res2.rental.id, res2.previous_reservation.rental.id)
        self.assertEquals(res7.rental.id, res7.previous_reservation.rental.id)
        self.assertFalse(res2.previous_reservation.rental.id == res7.previous_reservation.rental.id)

