from django.contrib.gis.db import models

from home.managers import PartQuerySet


class Building(models.Model):
    place = models.PointField()


class Level(models.Model):
    description = models.CharField(
        max_length=128)
    building = models.ForeignKey(
        to=Building,
        on_delete=models.CASCADE,
        related_name="levels",
        related_query_name="level")


class Room(models.Model):
    identifier = models.CharField(
        max_length=8)
    description = models.CharField(
        max_length=128)
    level = models.ForeignKey(
        to=Level,
        on_delete=models.CASCADE,
        related_name="rooms",
        related_query_name="room"
    )

    def __str__(self) -> str:
        return f"{self.identifier} - {self.description}"


class Surface(models.Model):
    width = models.FloatField()
    height = models.FloatField()
    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
        related_name="surfaces",
        related_query_name="surface")


class Part(models.Model):
    manufacturer = models.CharField(
        max_length=128)
    manufacturer_id = models.CharField(
        max_length=128)
    description = models.CharField(
        max_length=256)
    price = models.PositiveSmallIntegerField()

    objects = PartQuerySet.as_manager()

    def __str__(self) -> str:
        return f"{self.manufacturer} - {self.manufacturer_id}"


class Unit(models.Model):
    description = models.CharField(
        max_length=256)
    surface = models.ForeignKey(
        to=Surface,
        on_delete=models.SET_NULL,
        null=True,
        related_name="units",
        related_query_name="unit")
    parts = models.ManyToManyField(
        to=Part,
        related_name="units",
        related_query_name="unit")

    def __str__(self) -> str:
        return self.description
