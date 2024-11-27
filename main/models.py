from django.db import models


class Neighborhood(models.Model):
    title = models.CharField(max_length=200)
    chairman = models.CharField(max_length=250)
    MFY = models.CharField  (max_length=250)
    people = models.PositiveIntegerField(blank=True)
    area = models.DecimalField(decimal_places=2, max_digits=15)
    number_houses = models.IntegerField()
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


a_b = {
    'A':'A',
    'B':'B'
}

class House(models.Model):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices=a_b)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    people = models.PositiveIntegerField(blank=True)
    area = models.DecimalField(decimal_places=2, max_digits=15)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.house_boss