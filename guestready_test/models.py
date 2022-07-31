from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=255, default='')


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    @property
    def previous_reservation(self):
        """the reservation who's checkin date is most close to this reservation's checkin date

        :returns: the previous reservation to this reservation, or null
        :rtype: Reservation
        """
        older_reservations = Reservation.objects.filter(rental=self.rental, checkin__lt=self.checkin)
        previous_res = older_reservations.order_by('-checkin').first()
        return previous_res
