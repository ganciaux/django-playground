from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Person(models.Model):
    first_name = models.CharField("person's first name",max_length=30)
    last_name = models.CharField(max_length=30)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60, null=True)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE,verbose_name="the related musician", null=True)
    sites = models.ManyToManyField(Runner, verbose_name="list of runner", null=True)
    album = models.OneToOneField(Album,on_delete=models.CASCADE,verbose_name="related album", null=True)
    class Meta:
        db_table = 'Person'









