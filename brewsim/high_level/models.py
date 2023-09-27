# Create your models here.
from django.db import models


class Departement(models.Model):
    numero = models.IntegerField()
    prix_m2 = models.IntegerField()


class Machine(models.Model):
    nom = models.CharField(max_lenght=100)
    prix = models.IntegerField()


class Ingredient(models.Model):
    nom = models.CharField(max_lenght=100)


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_lenght=100)
    durée = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)


class Recette(models.Model):
    nom = models.CharField(max_lenght=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)


class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()


class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machine = models.ManyToMAnyField(Machine)
    recette = models.ManyToMAnyField(Recette)
    stock = models.ManyToMAnyField(QuantiteIngredient)


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()
