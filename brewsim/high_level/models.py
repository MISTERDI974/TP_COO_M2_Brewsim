# Create your models here.
from django.db import models


class Departement(models.Model):
    numero = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return "departement : " f"{self.numero}"

    def json(self):
        return {"numero ": self.numero, "prix_m2": self.prix_m2}


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    def __str__(self):
        return self.nom

    def cost(self):
        return self.prix

    def json(self):
        return {"nom ": self.nom.id, "prix": self.prix}


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom ": self.nom.id}


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

    def json(self):
        return {"ingredient ": self.ingredient.id, "quantite": self.quantite}


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return "Action : " f"{self.commande}"

    def json(self):
        return {
            "machine ": self.machine.id,
            "commande": self.commande,
            "duree ": self.duree,
            "ingredient": self.ingredient.id,
        }


class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom ": self.nom.id, "action": self.action}


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

    def json(self):
        tabMach = []
        tabRec = []
        tabStock = []

        for mach in self.machine.id:
            tabMach.append(mach)
        for rec in self.recette.id:
            tabRec.append(mach)
        for sto in self.stock.id:
            tabStock.append(mach)
        return {
            "departement ": self.departement.id,
            "taille": self.taille,
            "machine": tabMach,
            "recette": tabRec,
            "stock": tabStock,
        }

    def Achat_auto(self, rece):
        # peut etre améliorée pour acheter uniquement les ingrédients manquants
        print("debut achat auto")
        for ingre_Recette in rece.action.ingredient.all():
            print("dans le 1 for : ", ingre_Recette)
            print("STOCK : ", self.stock.all())
            for ingre_stock in self.stock.all():
                print("dans le 2 for : ", ingre_stock)
                if ingre_stock == ingre_Recette:
                    print("premier if")
                    if ingre_stock.quantite < ingre_Recette.quantite:
                        # Achat d'ingrédients pour le stock
                        print("second if")
                        self.stock.add(
                            QuantiteIngredient.object.create(ingre_Recette.quantite)
                        )

                        print(
                            "Achat ", ingre_Recette, " ", ingre_Recette.quantite, "Kg"
                        )


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient.nom}"
        " coûte " f"{self.prix} dans le " f"{self.departement.numero}"

    def json(self):
        return {
            "ingredient ": self.ingredient.id,
            "departement": self.departement,
            "prix": self.prix,
        }
