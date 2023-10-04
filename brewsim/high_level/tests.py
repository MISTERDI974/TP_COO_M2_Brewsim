from django.test import TestCase

from .models import (
    Action,
    Departement,
    Ingredient,
    Machine,
    Prix,
    QuantiteIngredient,
    Recette,
    Usine,
)


class MachineModelTests(TestCase):
    def test_usine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        self.assertEqual(Usine.objects.count(), 0)
        self.assertEqual(Ingredient.objects.count(), 0)
        self.assertEqual(Departement.objects.count(), 0)
        self.assertEqual(Action.objects.count(), 0)

        four = Machine.objects.create(nom="four", prix=1000)
        Chemine = Machine.objects.create(nom="Chemine", prix=2000)

        houblon = Ingredient.objects.create(nom="Houblon")
        orge = Ingredient.objects.create(nom="Orge")

        Quant_orge_init = QuantiteIngredient.objects.create(ingredient=orge, quantite=0)
        Quant_houblon_init = QuantiteIngredient.objects.create(
            ingredient=houblon, quantite=0
        )

        Haute_Garonne = Departement.objects.create(numero=31, prix_m2=2000)
        Prix.objects.create(ingredient=houblon, departement=Haute_Garonne, prix=20)
        Prix.objects.create(ingredient=orge, departement=Haute_Garonne, prix=10)

        Quant_houblon_31 = QuantiteIngredient.objects.create(
            ingredient=houblon, quantite=50
        )
        Quant_orge_31 = QuantiteIngredient.objects.create(ingredient=orge, quantite=100)

        Quant_orge_kaporal = Quant_orge_31
        Quant_orge_kaporal.quantite = Quant_orge_kaporal.quantite / 2

        Quant_houblon_kaporal = Quant_houblon_31
        Quant_houblon_kaporal.quantite = Quant_houblon_kaporal.quantite / 5

        cuire = Action.objects.create(machine=four, commande="cuire", duree=10)
        cuire.ingredient.add(Quant_houblon_kaporal)
        cuire.ingredient.add(Quant_orge_kaporal)

        kaporal = Recette.objects.create(nom="Kaporal", action=cuire)

        factory = Usine.objects.create(departement=Haute_Garonne, taille=50)

        factory.stock.add(Quant_orge_init)
        factory.stock.add(Quant_houblon_init)

        factory.machine.add(four)
        factory.machine.add(Chemine)

        # factory.stock.add(Quant_houblon_31)
        # factory.stock.add(Quant_orge_31)

        factory.recette.add(kaporal)

        self.assertEqual(Machine.objects.count(), 2)
        self.assertEqual(Usine.objects.count(), 1)
        self.assertEqual(Ingredient.objects.count(), 2)
        self.assertEqual(Departement.objects.count(), 1)
        self.assertEqual(Action.objects.count(), 1)

        factory.Achat_auto(kaporal)

        print("Cout usine =", factory.cost())
