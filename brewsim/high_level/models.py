# Create your models here.
from django.db import models


class Departement(models.Model):
    numero = models.IntegerField()
    prix_m2 = models.IntegerField()

    # def __str__(self):
    #    return "numero : " self.numero


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    # def __str__(self):
    # return "nom : " self.nom


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    durée = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)


class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)


class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()


class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machine = models.ManyToManyField(Machine)
    recette = models.ManyToManyField(Recette)
    stock = models.ManyToManyField(QuantiteIngredient)


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()
