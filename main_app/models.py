from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    price = models.CharField(max_length=10)


class FoodItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()


class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    food_items = models.ManyToManyField(FoodItem)
