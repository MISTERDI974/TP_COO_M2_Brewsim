from django.test import TestCase

from .models import Departement, Ingredient, Machine, Prix, QuantiteIngredient, Usine


class MachineModelTests(TestCase):
    def test_usine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        self.assertEqual(Usine.objects.count(), 0)
        self.assertEqual(Ingredient.objects.count(), 0)
        self.assertEqual(Departement.objects.count(), 0)

        four = Machine.objects.create(nom="four", prix=1000)
        Chemine = Machine.objects.create(nom="Chemine", prix=2000)

        houblon = Ingredient.objects.create(nom="Houblon")
        orge = Ingredient.objects.create(nom="Orge")

        Haute_Garonne = Departement.objects.create(numero=31, prix_m2=2000)
        Prix.objects.create(ingredient=houblon, departement=Haute_Garonne, prix=20)
        Prix.objects.create(ingredient=orge, departement=Haute_Garonne, prix=10)

        Quant_houblon_31 = QuantiteIngredient.objects.create(
            ingredient=houblon, quantite=50
        )
        Quant_orge_31 = QuantiteIngredient.objects.create(ingredient=orge, quantite=100)

        factory = Usine.objects.create(departement=Haute_Garonne, taille=50)

        factory.machine.add(four)
        factory.machine.add(Chemine)

        factory.stock.add(Quant_houblon_31)
        factory.stock.add(Quant_orge_31)

        self.assertEqual(Machine.objects.count(), 2)
        self.assertEqual(Usine.objects.count(), 1)
        self.assertEqual(Ingredient.objects.count(), 2)
        self.assertEqual(Departement.objects.count(), 1)

        print("Cout usine =", factory.cost())
