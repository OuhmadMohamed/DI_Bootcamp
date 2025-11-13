#Exercise 2 — Working with JSON
import json

# JSON fourni
sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Étape 1 : Charger le JSON
data = json.loads(sampleJson)

# Étape 2 : Accéder à la clé 'salary'
salary = data["company"]["employee"]["payable"]["salary"]
print("Salaire :", salary)

# Étape 3 : Ajouter la clé 'birth_date'
data["company"]["employee"]["birth_date"] = "1995-05-21"

# Étape 4 : Sauvegarder dans un fichier
with open("employee_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("\n JSON modifié sauvegardé dans 'employee_data.json'")
