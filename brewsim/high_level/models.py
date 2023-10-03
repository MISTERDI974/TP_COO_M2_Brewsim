# Create your models here.
from django.db import models


class Departement(models.Model):
    numero = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return "departement : " f"{self.numero}"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    def __str__(self):
        return self.nom

    def cost(self):
        return self.prix


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    durée = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)

    def __str__(self):
        return "Action : " f"{self.commande}"


class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient.nom}" " : " f"{self.quantite}" "Kg"

    def cost(self, departement):
        return self.quantite * self.ingredient.prix_set.get(departement.numero).prix


class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machine = models.ManyToManyField(Machine)
    recette = models.ManyToManyField(Recette)
    stock = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return "Usine " f"{self.departement}"

    def cost(self):
        prixTotalMachine = 0
        prixStock = 0
        for mach in self.machine:
            prixTotalMachine = prixTotalMachine + mach.cost()

        for ingre in self.stock:
            prixStock = prixStock + ingre.cost(self.departement)

        return self.taille * self.departement.prix_m2 + prixStock + prixTotalMachine


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient.nom}"
        " coûte " f"{self.prix} dans le " f"{self.departement.numero}"
