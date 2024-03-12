from django.db import models


class Ingridient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    steps = models.TextField()
    cooking_time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/')
    date_pub = models.DateTimeField(null=True)
    ingridients = models.ManyToManyField(Ingridient)
    categories = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.title)
