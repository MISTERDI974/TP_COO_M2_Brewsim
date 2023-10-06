#include <iostream>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>
using namespace std;
using json = nlohmann::json;

class Departement{
	int numero_;
	int prix_m2_;
	public :
		Departement(int a, int b): numero_{a}, prix_m2_{b} {};
		Departement(json data): numero_(data["numero"]), prix_m2_(data["prix_m2"]){};

		Departement(int id){
			string url = "http://localhost:8000/departement/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			numero_ = data["numero"];
			prix_m2_ = data["prix_m2"];
		};
		friend ostream& operator<<(ostream& out, const Departement& p){
			return out << p.numero_ << " / " << p.prix_m2_;
		}

};

class Machine{
	string nom_;
	int prix_;

	public:
		Machine(int id){
			string url = "http://localhost:8000/machine/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			nom_ = data["nom"];
			prix_ = data["prix"];
		};

		friend ostream& operator<<(ostream& out, const Machine& p){
			return out << p.nom_ << " / " << p.prix_;
		}

};


class Ingredient{
	string nom_;

	public:
		Ingredient(int id){
			string url = "http://localhost:8000/ingredient/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			nom_ = data["nom"];
		};

		friend ostream& operator<<(ostream& out, const Ingredient& p){
			return out << p.nom_;
		}

};


class QuantiteIngredient{
	unique_ptr<Ingredient> ingredient_;
	int quantite_;

	public:
		QuantiteIngredient(int id){
			string url = "http://localhost:8000/quantiteingredient/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			ingredient_ = make_unique<Ingredient>(data["ingredient"]);
			quantite_ = data["quantite"];
		};

	friend ostream& operator<<(ostream& out, const QuantiteIngredient& p){
			return out << *p.ingredient_ << " / " << p.quantite_;
		}
};


class Action{
	unique_ptr<Machine> machine_;
	string commande_;
	int duree_;
	vector<unique_ptr<Ingredient>> ingredient_;

	public:
		Action(int id){
			string url = "http://localhost:8000/action/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			machine_ = make_unique<Machine>(data["machine"]);
			commande_ = data["commande"];
			duree_ = data["duree"];

			for(const auto &i : data["ingredient"])
			{
					//cout << data["ingredient"] << endl ;
					// << i << endl;
					ingredient_.push_back(make_unique<Ingredient>(i));
				//	cout << *ingredient_.back() << endl ;
			}
		};

		friend ostream& operator<<(ostream& out, const Action& p){
			out << *p.machine_ << " / " << p.commande_ <<" / " << p.duree_  <<" / ";
			for (const auto &i : p.ingredient_)
			{
				out << *i;
			}
			return out;
		}
};

class Recette{
	string nom_;
	unique_ptr<Action> action_;

	public:
		Recette(int id){
			string url = "http://localhost:8000/recette/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			nom_ = data["nom"];
			action_ = make_unique<Action>(data["action"]);
		};

		/*friend ostream& operator<<(ostream& out, const Recette& p){
			return out << p.nom_ << " / " << p.action_;
		}*/
};


class Usine{
	unique_ptr<Departement> departement_;
	int taille_;
	unique_ptr<Machine> machine_;
	unique_ptr<Recette> recette_;
	unique_ptr<QuantiteIngredient> stock_;


	public:
	/*	Usine(int id){
			string url = "http://localhost:8000/usine/" + to_string(id);
			cpr::Response r = cpr::Get(cpr::Url{url});
			json data = json::parse(r.text);
			nom_ = data["nom"];
			taille_ = data["taille"];
			machine_ = make_unique<Action>(data["machine"]);
			recette_ = make_unique<Action>(data["recette"]);
			stock_ = make_unique<Action>(data["stock"]);
		};*/
};


class Prix{
	unique_ptr<Ingredient> ingredient_;
	unique_ptr<Departement> departement_;
	int prix_;

	public:
};
/////////////MAIN//////////////////////
int main(void)
{
	//Ingredient a(1);
//// 	QuantiteIngredient b(1);
	Action c(1);
//	cout << a << endl;
//	cout << b << endl;
cout << c << endl;
	return 0;
}
