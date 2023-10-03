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


class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient.nom}" " : " f"{self.quantite}" "Kg"

    def cost(self, dep):
        return (
            self.quantite
            * self.ingredient.prix_set.get(departement__numero=dep.numero).prix
        )


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return "Action : " f"{self.commande}"


class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


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
        for mach in self.machine.all():
            prixTotalMachine = prixTotalMachine + mach.cost()

        for ingre in self.stock.all():
            prixStock = prixStock + ingre.cost(self.departement)

        return self.taille * self.departement.prix_m2 + prixStock + prixTotalMachine

    def Achat_auto(self, rece):
        # peut etre améliorée pour acheter uniquement les ingrédients manquants
        for ingre_Recette in rece.action.ingredient.all():
            if self.stock.ingre_Recette.quantite < ingre_Recette.quantite:
                # Achat d'ingrédients pour le stock
                self.stock.add(QuantiteIngredient.object.create(ingre_Recette.quantite))

                print("Achat ", ingre_Recette, " ", ingre_Recette.quantite, "Kg")


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient.nom}"
        " coûte " f"{self.prix} dans le " f"{self.departement.numero}"
